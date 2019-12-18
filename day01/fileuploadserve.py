# coding=utf-8

#文件上传工具

import socket

HOST = ''
PORT = 8888

filename = '../datas/wine.csv'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as so:
    so.bind((HOST, PORT))
    so.listen(10)
    print('服务器启动...')

    while True:
        with so.accept()[0] as conn:
            #创建字节序列对象列表，作为接CCASP数据的缓冲区
            buffer = []
            while True: #反复接受数据
                data = conn.recv(1024)
                if data:
                    #接受的数据添加到缓冲区
                    buffer.append(data)
                else:
                    #没有接受到数据则退出
                    break
            #将接受到的字节序列到对象列表合并为一字节序列对象
            b = bytes().join(buffer)
            with open(filename, 'wb') as f:
                f.write(b)

            print('服务器接受完成。')