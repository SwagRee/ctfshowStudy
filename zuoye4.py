# 初始化三个活动的报名列表
badminton = []
volunteer = []
climbing = []

# 主菜单循环
while True:
    print("\n1: 报名打羽毛球。")
    print("2: 报名做义工。")
    print("3: 报名爬山。")
    print("4: 表示退出。")
    choice = input("请输入选择：")

    if choice == '1':
        # 打羽毛球报名
        print("请输入打羽毛球信息（输入4退出）：")
        while True:
            info = input("请输入打羽毛球信息：")
            if info == '4':
                break
            badminton.append(info)

    elif choice == '2':
        # 做义工报名
        print("请输入做义工信息（输入4退出）：")
        while True:
            info = input("请输入做义工信息：")
            if info == '4':
                break
            volunteer.append(info)

    elif choice == '3':
        # 爬山报名
        print("请输入爬山信息（输入4退出）：")
        while True:
            info = input("请输入爬山信息：")
            if info == '4':
                break
            climbing.append(info)

    elif choice == '4':
        break  # 退出主程序

    else:
        print("无效选择，请重新输入！")

# 统计三个活动都报名的人员
set_badminton = set(badminton)
set_volunteer = set(volunteer)
set_climbing = set(climbing)
common = set_badminton & set_volunteer & set_climbing
common_list = sorted(list(common))  # 按字母顺序排序

# 输出结果
print("\n打羽毛球：", badminton)
print("做义工：", volunteer)
print("爬山：", climbing)
print("三个活动都报名的学生：", common_list)
print("三个活动都报名的人数：", len(common_list))