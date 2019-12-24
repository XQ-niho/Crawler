# coding=utf-8

# 爬取图片

import urllib.request

import os
import re

url = 'http://p.weather.com.cn/'

def findallimagerurl(htmlstr):
    """
    从HTML代码中查找匹配的字符串
    :param htmlstr:
    :return:
    """
    # 定义正则表达式
    pattern = r'http://\S+(?:\.png|\.jpg)'
    return re.findall(pattern, htmlstr)

def getfilename(urlstr):
    # 根据图片链接地址截取图片名
    pos = urlstr.rfind('/')
    return urlstr[pos + 1: ]

# 分析获得url列表
url_list = []
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()

    url_list = findallimagerurl(htmlstr)

for imagersrc in url_list:
    # 根据图片地址下载
    req = urllib.request.Request(imagersrc)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        # 过滤掉小余10KB的图片
        if len(data) < 1024 * 100:
            continue

        # 创建文件夹
        if not os.path.exists('download'):
            os.mkdir('download')

        # 获得图片文件名
        filename = getfilename(imagersrc)
        filename = 'download/' + filename

        # 保存图片到本地
        with open(filename, 'wb') as f:
            f.write(data)
    print('下载图片',filename)