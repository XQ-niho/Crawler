# coding=utf-8

import configparser

config = configparser.ConfigParser()

config.read('../datas/Setup.ini', encoding='utf-8')

print(config.sections()) #返回所有的节

section = config['Startup']
print(config['Startup']) #返回指定节

print(config.options('Startup')) #返回该节下的所有配置项

#返回指定节与指定项的值
print(section['RequireOS'])
print(config['Startup']['RequireOS'])

value = config.get('Startup', 'RequireOS')
print(value)
value1 = config.getint('Window 2000', 'MajorVersion')
print(value1)