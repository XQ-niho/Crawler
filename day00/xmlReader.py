# coding=utf-8

import xml.etree.ElementTree as ET

tree = ET.parse('../datas/Notes.xml')

root = tree.getroot() #得到根元素

for index, child in enumerate(root):
    # tag属性：获得当前元素标
    # attrib属性：获得当前元素的属性
    print('第{0}个{1}元素，属性：{2}'.format(index, child.tag, child.attrib))
    for i, child_child in enumerate(child):
        print('     标签：{0}，内容：{1}'.format(child_child.tag, child_child.text))