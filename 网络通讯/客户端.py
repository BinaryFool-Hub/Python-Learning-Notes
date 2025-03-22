import socket

# 创建 socket 对象
#   socket.AF_INET ipv4 协议（版本）
#   socket.SOCK_STREAM   tcp 协议
tcp_client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 指定服务器连接的端口
tcp_client_server.connect(('127.0.0.1', 7788))  # 接收元组类型数据

state_info = '退出连接'
while True:
    # 接受服务器的数据
    tcp_server_data = tcp_client_server.recv(1024)  # 1024字节，指定最大可以接受多大的数据
    print(f'服务器：{tcp_server_data.decode("utf-8")}')

    # 发送数据给服务器
    user_input = input('输入发送的内容：')
    tcp_client_server.send(user_input.encode('utf-8'))

    # 断开连接
    if user_input == state_info:
        break

# 关闭客户端
tcp_client_server.close()
