# coding=utf-8

#服务端

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 8888))
print('服务器启动...')

#从客户端接收数据
data, client_address = s.recvfrom(1024)
print(client_address)
print('从客户端接收的消息：{0}'.format(data.decode()))

#给客户端发送消息
s.sendto('你好'.encode(), client_address)

#释放资源
s.close()