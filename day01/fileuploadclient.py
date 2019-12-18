# coding=utf-8

#客户端

import socket

HOST = '127.0.0.1'
PORT = 8888

filename = "../datas/winequalityred.csv"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as so:

    so.connect((HOST, PORT))

    with open(filename, 'rb') as f:
        b = f.read()
        so.sendall(b)
        print('客户端上传数据完成。')