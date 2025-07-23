#郑鹏来
# 管理员信息
admin_user = "admin"
admin_pass = "admin"

# 会员信息存储字典
members = {}

# 管理员登录验证
def admin_login():
    username = input("管理员用户名: ")
    password = input("管理员密码: ")
    return username == admin_user and password == admin_pass

# 主菜单功能
def manage_members():
    while True:
        print("\n1. 添加会员\n2. 删除会员\n3. 查看会员\n4. 退出")
        choice = input("请输入选项: ")
        if choice == '1':
            username = input("输入用户名: ")
            if username in members:
                print("用户已存在！")
            else:
                password = input("输入密码: ")
                members[username] = password
                print("添加成功！")
        elif choice == '2':
            username = input("输入用户名: ")
            if username in members:
                del members[username]
                print("删除成功！")
            else:
                print("用户不存在！")
        elif choice == '3':
            print("\n所有会员信息:")
            for user, pwd in members.items():
                print(f"用户名: {user}, 密码: {pwd}")
        elif choice == '4':
            break
        else:
            print("无效选项！")

# 主程序
if admin_login():
    manage_members()
else:
    print("管理员登录失败！")