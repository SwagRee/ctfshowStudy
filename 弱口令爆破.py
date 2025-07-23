import jwt
import itertools

def generate_passwords(max_length=8):
    """生成1到max_length位的密码，包含数字、小写字母和大写字母"""
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for length in range(1, max_length + 1):
        for password in itertools.product(characters, repeat=length):
            yield ''.join(password)

def detect_weak_jwt(token):
    """尝试使用1到8位密码（包含数字、小写字母和大写字母）破解JWT"""
    for password in generate_passwords():
        try:
            # 尝试使用当前密码解码JWT
            decoded = jwt.decode(token, password, algorithms=['HS256'])
            print(f"弱口令检测成功！使用的密码是: {password}")
            print(f"解码后的JWT内容: {decoded}")
            return password
        except jwt.InvalidTokenError:
            continue
        except jwt.DecodeError:
            continue
    print("未找到匹配的弱口令。")
    return None

if __name__ == "__main__":
    # 你的 JWT
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTc0MTg2OTk2NiwiZXhwIjoxNzQxODc3MTY2LCJuYmYiOjE3NDE4Njk5NjYsInN1YiI6InVzZXIiLCJqdGkiOiI3YzJhZGFlYjk2ZDIyNmI5YmY2OTAzODlhYjk0MzdhYyJ9.8GZ1E4QvEbIlSeCsI3SugX59p-3CiJ4kmV7yBxyFKGg"
    # 检测弱口令
    detect_weak_jwt(token)