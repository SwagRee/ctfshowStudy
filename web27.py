def generate_birthday_dict(start_year=1900, end_year=2023, filename="birthday_dict.txt"):
    """
    生成出生年月字典 (YYYYMMDD格式)

    参数:
        start_year: 起始年份 (默认1900)
        end_year: 结束年份 (默认2023)
        filename: 输出文件名
    """
    with open(filename, 'w') as f:
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                # 确定每个月的天数
                if month in [4, 6, 9, 11]:
                    max_day = 30
                elif month == 2:
                    # 闰年判断
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        max_day = 29
                    else:
                        max_day = 28
                else:
                    max_day = 31

                for day in range(1, max_day + 1):
                    # 格式化为YYYYMMDD，保证两位数月份和日期
                    birthday = f"{year}{month:02d}{day:02d}"
                    f.write(birthday + "\n")

    print(f"字典已生成，保存到 {filename}")


# 使用示例（生成1950-2025年的生日字典）
generate_birthday_dict(start_year=1950, end_year=2025)