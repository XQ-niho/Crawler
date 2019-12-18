# coding=utf-8

# urllib.request.urlopen()的使用

import urllib.request

with urllib.request.urlopen('http://www.sina.com.cn') as response:
    data = response.read()
    html = data.decode()
    print(html)