# coding=utf-8

import configparser

config = configparser.ConfigParser()

config.read('../datas/Setup.ini', encoding='utf-8')

#写入配置文件
config['Startup']['RequireMIS'] = '8.0'

config.add_section('Section2') #添加节
config.set('Section2', 'name', 'Mac') #添加配置项name = Mac

with open('../datas/Setup.ini', 'w') as wf:
    config.write(wf)