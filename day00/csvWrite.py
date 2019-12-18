# coding=utf-8

import csv

with open('../datas/winequalityred.csv', 'r', encoding='gbk') as rfile:
    reader = csv.reader(rfile)
    with open('../datas/write.csv', 'w', newline='', encoding='gbk') as wfile:
        writer = csv.writer(wfile, delimiter='\t')
        for row in reader:
            writer.writerow(row)