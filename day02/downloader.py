# coding=utf-8

# 下载程序

import urllib.request

url = 'http://localhost:88/index.php'

with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = '../datas/download.php'
    with open(f_name, 'wb') as f:
        f.write(data)
        print('下载文件成功')