import socket

# 创建 socket 对象
#   socket.AF_INET ipv4 协议（版本）
#   socket.SOCK_STREAM   tcp 协议
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和端口
# 电脑里面端口号的数量0~65535
tcp_server_socket.bind(('127.0.0.1', 7788))  # 传入的需要是元组类型

# 监听客户端连接数量最大
# 最大可以允许多个客户端访问我的服务器(超过最大同时访问数,网址的崩溃)
tcp_server_socket.listen(124)

# 等待客户端连接
#   tcp_client_socket   与客户端的链接（会话）
#   tcp_client_address  客户端的地址(电脑的ip + port)
tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
# print(f'客户端已经连接， {tcp_client_socket, tcp_client_address}')
print(f'{tcp_client_address}客户端已经连接')

# 数据收发
# 网络通讯是以二进制模式通讯，所以需要进行编码
tcp_client_socket.send('你成功连接服务端'.encode('utf-8'))
state_info = '退出连接'
while True:
    # 接受客户端的信息
    client_data = tcp_client_socket.recv(1024)  # 1024字节，指定最大可以接受多大的数据
    client_state_info = client_data.decode('utf-8')

    # 断开连接
    if client_state_info == state_info:
        break

    print(f"{tcp_client_address}：{client_state_info}")

    # 服务端发送的信息
    server_data = input('输入服务端发送的信息：')
    tcp_client_socket.send(server_data.encode('utf-8'))

# 关闭客户端连接
print(f'{tcp_client_address}退出系统')
tcp_client_socket.close()

# 关闭服务器连接,一般情况服务器都是24小时运行，不会进行关闭
# tcp_server_socket.close()
