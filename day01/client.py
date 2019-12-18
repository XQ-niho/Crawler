# coding=utf-8

#客户端

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接服务器
s.connect(('127.0.0.1', 8888))

#给服务端发送数据
s.send(b'hello')

#从服务端接受数据
data = s.recv(1024)
print('从服务端接受的消息：{0}'.format(data.decode()))

#释放资源
s.close()