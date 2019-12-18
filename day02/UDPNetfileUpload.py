# coding=utf-8

#文件上传服务端

import socket

HOST = '127.0.0.1'

PORT = 8888

f_name = '../datas/test_copy.txt'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as so:
    so.bind((HOST, PORT))
    print('服务器启动...')

    # 创建字节序列对象列表，作为接收数据的缓冲区
    buffer = []
    while True:
        data, _ = so.recvfrom(1024)
        if data:
            flag = data.decode()
            if flag == 'bye':
                break
            buffer.append(data)
        else:
            #没有接收到数据，进入下次循环继续接收
            continue
    #将接收的字节序列对象列表合并成为一字节序列对象
    b = bytes().join(buffer)
    with open(f_name, 'w') as f:
        f.write(b.decode())

    print('服务器接收完成。')