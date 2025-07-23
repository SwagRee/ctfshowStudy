# dic = {"ccg": "123456", "lzc": "abcdefg", "zy": "basdfsdf", "zcw": "1123123basdfsdf"}
# attempts = 0
#
# while attempts < 5:
#     user = input("用户名: ")
#     pwd = input("密码: ")
#     if dic.get(user) == pwd:
#         print("登录成功！")
#         break
#     else:
#         attempts += 1
#         print(f"错误！剩余尝试次数: {5 - attempts}")
# else:
#     print("错误次数过多，程序退出！")

dic = {"ccg": "123456", "lzc": "abcdefg", "zy": "basdfsdf", "zcw": "1123123basdfsdf"}
# user = input("用户名: ")
# pwd = input("密码: ")
#
# if user in dic:
#     print("用户已存在！")
# else:
#     dic[user] = pwd
#     print("用户添加成功！")
# dic = {"ccg": "123456", "lzc": "abcdefg", "zy": "basdfsdf", "zcw": "1123123basdfsdf"}
user = input("用户名: ")

if user in dic:
    del dic[user]
    print("用户删除成功！")
else:
    print("用户不存在！")