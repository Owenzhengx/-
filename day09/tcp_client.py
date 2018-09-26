# tcp客户端流程
# tcp客户端流程

from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 发起连接
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

while True:
    # 消息发送接收
    data = input('发送>>>')
    if not data:
        break
    sockfd.send(data.encode())  # 将字符串转成bytes格式
    data =sockfd.recv(2014)
    print('接收到：',data.decode())

#　关闭套接字
sockfd.close()




