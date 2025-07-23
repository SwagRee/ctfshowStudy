import hashlib

target_hash = '084BBE17CEC67E1D138F01A54D650F8D'

def check_md5(s):
    # 计算字符串的MD5哈希并转换为大写
    return hashlib.md5(s.encode('utf-8')).hexdigest().upper() == target_hash

found = False

# 遍历5到10位数字
for digits in range(5, 11):
    print(f"正在检查 {digits} 位数字...")
    # 生成当前位数的所有可能数字（包含前导零）
    for num in range(0, 10 ** digits):
        # 转换为字符串并补零至指定位数
        s = str(num).zfill(digits)
        if check_md5(s):
            print(f"找到匹配的数字：{s}")
            found = True
            break
    if found:
        break

if not found:
    print("未找到匹配的数字。")