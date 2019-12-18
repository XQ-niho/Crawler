# coding=utf-8

import json

#从字符串解码
json_obj = r'{"name": "tony", "ang": 30, "sex": true, "a": [1, 3], "b": ["A", "B", "C"]}'

py_dict = json.loads(json_obj)
print(py_dict)

py_list = py_dict['a']
py_list1 = py_dict['b']
print(py_list)
print(py_list1)

#从文件中解码
with open('../datas/data2.json', 'r') as rf:
    data = json.load(rf)
    print(data)