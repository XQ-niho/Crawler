# coding=utf-8

#POST请求

import urllib.request
import urllib.parse

url = 'http://www.51work6.com/service/mynotes/WebService.php'

#准备http请求参数
params_dict = {
    'email': '2252984586@qq.com',
    'type': 'JSON',
    'action': 'query',
}
#将普通字符串转换为url编码字符串
params_str = urllib.parse.urlencode(params_dict)
#POST请求时参数要求以字节形式发送
params_bytes = params_str.encode()#字符串转换为字节序列对象

req = urllib.request.Request(url, data = params_bytes)

with urllib.request.urlopen(url) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)