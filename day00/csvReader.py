# coding=utf-8

import csv

with open ('../datas/winequalityred.csv', 'r', encoding='gbk') as file:
    reader = csv.reader(file, dialect=csv.excel)
    for row in reader:
        print('|'.join(row))