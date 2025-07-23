import jwt
import os

# 读取私钥文件
current_dir = os.getcwd()
private_key_path = os.path.join(current_dir, 'public.key')  # 确保这是您的私钥文件

try:
    with open(private_key_path, 'r') as key_file:
        private_key = key_file.read()
except FileNotFoundError:
    print(f"私钥文件未找到: {private_key_path}")
    exit(1)
except IOError:
    print(f"读取私钥文件时出错: {private_key_path}")
    exit(1)

# 生成 JWT
payload = {'user': 'admin'}
# 注意：HS256 使用对称加密，需要的是共享密钥。如果 'public.key' 是私钥，可能您需要使用 RS256 等非对称算法。
# 如果确实需要使用 HS256，请确保使用的是共享密钥而不是公钥或私钥。

token = jwt.encode(payload, private_key, algorithm='HS256')
print(token)