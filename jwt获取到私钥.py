import jwt
private = open('E://Resource//private.key', 'r').read()
header = {
    "alg": "RS256",
    "typ": "JWT"
}
payload={
    "user":"admin",
    "iat": 1714555712
}
token = jwt.encode(
    payload=payload,
    key=private, # 密钥
    algorithm="RS256", # 加密方式
    headers=header
)
print(token)
