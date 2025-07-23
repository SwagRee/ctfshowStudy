from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import yaml
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'static/uploads'
DATA_FILE = 'tickets.yml'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def load_tickets():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or []
    except (FileNotFoundError, yaml.YAMLError):
        return []


def save_tickets(tickets):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(tickets, f, allow_unicode=True, default_flow_style=False)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def check_recent_submission(ip):
    # 开发调试模式跳过限制
    if app.debug and ip == '127.0.0.1':
        return False

    tickets = load_tickets()
    now = datetime.now()
    for ticket in tickets:
        if ticket['ip'] == ip:
            submit_time = datetime.fromisoformat(ticket['submit_time'])
            if now - submit_time < timedelta(hours=24):
                return True
    return False


@app.route('/api/ticket', methods=['POST'])
def submit_ticket():
    try:
        ip = request.remote_addr

        if check_recent_submission(ip):
            return jsonify(
                success=False,
                message="24小时内只能提交一个工单",
                error_code="SUBMISSION_LIMIT_EXCEEDED"
            ), 429

        required_fields = ['game_name', 'zone', 'qq_number', 'feedback']
        if not all(field in request.form for field in required_fields):
            return jsonify(success=False, message="缺少必填字段"), 400

        ticket_id = str(uuid.uuid4())[:8]
        submit_time = datetime.now().isoformat()
        images = []

        # 处理文件上传
        for i in range(1, 3):
            file_key = f'image{i}'
            if file_key not in request.files:
                continue

            file = request.files[file_key]
            if file and file.filename != '':
                if file.content_length > MAX_FILE_SIZE:
                    return jsonify(
                        success=False,
                        message=f"图片{i}大小超过5MB限制"
                    ), 400

                if not allowed_file(file.filename):
                    return jsonify(
                        success=False,
                        message=f"图片{i}格式不支持"
                    ), 400

                ext = os.path.splitext(file.filename)[1]
                filename = f"{ticket_id}_{i}{ext}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                images.append(filename)

        new_ticket = {
            "ticket_id": ticket_id,
            "game_name": request.form['game_name'],
            "zone": request.form['zone'],
            "qq_number": request.form['qq_number'],
            "feedback": request.form['feedback'],
            "submit_time": submit_time,
            "status": "待处理",
            "complete_time": None,
            "remark": None,
            "ip": ip,
            "images": images
        }

        tickets = load_tickets()
        tickets.append(new_ticket)
        save_tickets(tickets)

        return jsonify(success=True, ticket_id=ticket_id)

    except Exception as e:
        app.logger.error(f"工单提交失败: {str(e)}")
        return jsonify(
            success=False,
            message="服务器处理请求时发生错误",
            error_code="INTERNAL_SERVER_ERROR"
        ), 500


@app.route('/api/ticket/status/ip', methods=['GET'])
def get_tickets_by_ip():
    try:
        ip = request.remote_addr
        tickets = load_tickets()
        user_tickets = [t for t in tickets if t['ip'] == ip]

        formatted_tickets = []
        for t in user_tickets:
            formatted = {
                "工单 ID": t['ticket_id'],
                "提交时间": datetime.fromisoformat(t['submit_time']).strftime('%Y-%m-%d %H:%M:%S'),
                "状态": t['status'],
                "备注": t['remark'],
                "问题描述": t['feedback'],
                "图片": [f"/{app.config['UPLOAD_FOLDER']}/{img}" for img in t['images']]
            }

            if t['complete_time']:
                formatted["完成时间"] = datetime.fromisoformat(t['complete_time']).strftime('%Y-%m-%d %H:%M:%S')

            formatted_tickets.append(formatted)

        return jsonify(success=True, tickets=formatted_tickets)

    except Exception as e:
        app.logger.error(f"工单查询失败: {str(e)}")
        return jsonify(
            success=False,
            message="查询工单时发生错误",
            error_code="INTERNAL_SERVER_ERROR"
        ), 500


@app.route('/api/reset', methods=['POST'])
def reset_system():
    """测试用重置端点"""
    try:
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)

        for filename in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)

        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500


# 新增配置
ADMIN_PASSWORD = "admin123"  # 管理密码
UPLOAD_FOLDER = 'static/uploads'
DATA_FILE = 'tickets.yml'


# ... 保持原有代码不变 ...

# 新增管理API端点
@app.route('/api/admin/tickets', methods=['GET'])
def get_all_tickets():
    # 简单的密码验证
    if request.headers.get('X-Admin-Password') != ADMIN_PASSWORD:
        return jsonify(success=False, message="Unauthorized"), 401

    tickets = load_tickets()
    return jsonify(success=True, tickets=tickets)


@app.route('/api/ticket/<ticket_id>/status', methods=['PUT'])
def update_status(ticket_id):
    if request.headers.get('X-Admin-Password') != ADMIN_PASSWORD:
        return jsonify(success=False, message="Unauthorized"), 401

    new_status = request.json.get('status')
    if new_status not in ['待处理', '已处理']:
        return jsonify(success=False, message="Invalid status"), 400

    tickets = load_tickets()
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id:
            ticket['status'] = new_status
            if new_status == '已处理':
                ticket['complete_time'] = datetime.now().isoformat()
            save_tickets(tickets)
            return jsonify(success=True)

    return jsonify(success=False, message="Ticket not found"), 404


@app.route('/api/ticket/<ticket_id>/remark', methods=['PUT'])
def update_remark(ticket_id):
    if request.headers.get('X-Admin-Password') != ADMIN_PASSWORD:
        return jsonify(success=False, message="Unauthorized"), 401

    new_remark = request.json.get('remark', '')

    tickets = load_tickets()
    for ticket in tickets:
        if ticket['ticket_id'] == ticket_id:
            ticket['remark'] = new_remark
            save_tickets(tickets)
            return jsonify(success=True)

    return jsonify(success=False, message="Ticket not found"), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)