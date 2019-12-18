# coding=utf-8

import json

py_dict = {'name': 'tony', 'age': 30, 'sex': True}
py_list = [1,2,3]
py_tuple = ('A', 'B', 'C')

py_dict['a'] = py_list
py_dict['b'] = py_tuple

#编码
jsonObj = json.dumps(py_dict)
print(jsonObj)

#格式化编码
jsonObj002 = json.dumps(py_dict, indent=4)
print(jsonObj002)

#写入JSON到文件
with open('../datas/data1.json', 'w') as wf:
    json.dump(py_dict, wf)

#写入格式化JSON到文件
with open('../datas/data2.json', 'w') as wf:
    json.dump(py_dict, wf, indent=4)