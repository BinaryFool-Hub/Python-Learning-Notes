import socket
import threading
import tkinter as tk
from tkinter import ttk


class NetGui:
    def __init__(self, window_size="650x500+50+50"):
        self.root = tk.Tk()
        self.root.title("%s v%s" % ("网络调试助手", "0.0.1"))
        self.root.geometry(window_size)
        self.root.resizable(width=False, height=False)

        # 服务器协议
        self.agreement_type_variable = tk.StringVar()
        self.agreement_type_variable.set("TCP 服务器")
        # 本地主机地址
        self.host_variable = tk.StringVar()
        self.host_variable.set("127.0.0.1")

        # 本机开放端口
        self.port_var = tk.StringVar()
        self.port_var.set("7788")

        # 接收数据解码方式
        self.recv_hex_var = tk.IntVar()  # 1 utf-8 2 gbk
        self.recv_hex_var.set(1)
        # 接收数据多选框  框1 时候使用json解码

        self.recv_v_int = [tk.IntVar(), tk.IntVar()]
        # 提前选择内容

        # 发送数据编码方式
        self.send_hex_var = tk.IntVar()  # 1 utf-8 0 gbk
        self.send_hex_var.set(1)
        # 发送数据多选框
        self.send_v_int = [tk.IntVar(), tk.IntVar()]
        # # 提前选择内容

        # 获取本机的 ip 地址
        try:
            print("socket.gethostname()", socket.gethostname())
            ip_name = socket.getfqdn(socket.gethostname())
            my_address = socket.gethostbyname(ip_name)
            hosts_list = (my_address, "127.0.0.1")
        except Exception as e:
            hosts_list = ("127.0.0.1",)

        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)

        network_frame = tk.LabelFrame(left_frame, text="网络设置", pady=5, padx=5)
        network_frame.pack()

        tk.Label(network_frame, text="(1) 协议类型").pack(anchor=tk.W)
        w = ttk.Combobox(
            network_frame,
            textvariable=self.agreement_type_variable,
            values=("TCP 服务器", "TCP 客户端"),
        )
        w.pack(fill=tk.X)

        tk.Label(network_frame, text="(2) 本地主机地址").pack(anchor=tk.W)
        host = ttk.Combobox(
            network_frame, textvariable=self.host_variable, values=hosts_list
        )
        host.pack(fill=tk.X)

        tk.Label(network_frame, text="(3) 本地端口").pack(anchor=tk.W)
        port = tk.Entry(network_frame, textvariable=self.port_var)
        port.pack()

        """button按钮布局"""
        button_frame = tk.Frame(network_frame)
        button_frame.pack()

        self.connect_button_open = tk.Button(button_frame, text="打开")
        self.connect_button_open.pack(side=tk.LEFT)
        self.connect_button_close = tk.Button(button_frame, text="关闭")
        self.connect_button_close.pack()

        """接收数据"""
        recv_setting_frame = tk.LabelFrame(left_frame, text="接收设置", pady=5, padx=5)
        recv_setting_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)

        tk.Radiobutton(
            recv_setting_frame, text="utf-8", variable=self.recv_hex_var, value=1
        ).pack(anchor=tk.W)
        tk.Radiobutton(
            recv_setting_frame, text="gbk", variable=self.recv_hex_var, value=2
        ).pack(anchor=tk.W)

        tk.Checkbutton(
            recv_setting_frame, text="json数据", variable=self.recv_v_int[0]
        ).pack(anchor="w")
        tk.Checkbutton(
            recv_setting_frame, text="自动换行", variable=self.recv_v_int[1]
        ).pack(anchor="w")

        """发送数据"""
        send_setting_frame = tk.LabelFrame(left_frame, text="发送设置", pady=5, padx=5)
        send_setting_frame.pack(anchor=tk.N, fill=tk.X)

        tk.Radiobutton(
            send_setting_frame, text="utf-8", variable=self.send_hex_var, value=1
        ).pack(anchor=tk.W)
        tk.Radiobutton(
            send_setting_frame, text="gbk", variable=self.send_hex_var, value=0
        ).pack(anchor=tk.W)

        tk.Checkbutton(
            send_setting_frame, text="数据加密(未实现)", variable=self.send_v_int[0]
        ).pack(anchor="w")
        tk.Checkbutton(
            send_setting_frame, text="信息接受(未实现)", variable=self.send_v_int[1]
        ).pack(anchor="w")

        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.TOP, padx=5, pady=5)

        info_frame = tk.Frame(right_frame)
        info_frame.pack()

        tk.Label(info_frame, text="数据日志").pack(anchor=tk.W)
        self.text_area = tk.Text(info_frame, width=62)
        self.text_area.pack(side=tk.LEFT, fill=tk.X)

        send_scr_bar = tk.Scrollbar(info_frame)
        send_scr_bar.pack(side=tk.RIGHT, fill=tk.Y)
        # 设置 text_area 的 y 坐标为滚动条
        self.text_area.config(yscrollcommand=send_scr_bar.set)
        # 设置滚动条的命令为 text_area 的 y 视图
        send_scr_bar.config(command=self.text_area.yview)

        tk.Label(right_frame, text="信息发送").pack(anchor=tk.W)
        send_frame = tk.Frame(right_frame)
        send_frame.pack(side=tk.LEFT, fill=tk.X)

        self.send_area = tk.Text(send_frame, width=60, height=6)
        self.send_area.pack(side=tk.LEFT)
        self.send_button = tk.Button(send_frame, text="发送", width=8)
        self.send_button.pack(side=tk.LEFT, fill=tk.Y)

    # tkinter逻辑
    def insert_to_text(self, data):
        self.text_area.insert(tk.END, ">>> " + data + "\n")


class Net(NetGui):
    def __init__(self):
        self.run_flag = False  # 标记是否已经启动

        super().__init__("650x500+50+50")
        self.port = int(self.port_var.get())
        self.host = self.host_variable.get()
        self.connect_button_open.config(command=self.open_tcp_connect)
        self.root.mainloop()

    @property
    def __address(self):
        return self.host_variable.get(), int(self.port_var.get())

    @property
    def __send_str_code(self):
        return "utf-8" if self.send_hex_var.get() else "gbk"

    @property
    def __recv_str_code(self):
        return "utf-8" if self.recv_hex_var.get() else "gbk"

    def create_server_socket(self, inet=socket.AF_INET, sock=socket.SOCK_STREAM):
        """
        创建服务器连接
        """
        # 创建socket
        self.tcp_server_socket = socket.socket(inet, sock)
        # 绑定
        self.tcp_server_socket.bind(self.__address)
        # 等待接收客户端的请求
        self.tcp_server_socket.listen(128)

    def listing_connect(self):
        """"""
        while True:
            # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
            # client_socket 用来为这个客户端服务
            # tcp_server_socket 就可以省下来专门等待其他新客户端的链接
            self.client_socket, client_addr = self.tcp_server_socket.accept()
            self.insert_to_text(f"客户端:{client_addr} 已经链接服务")
            r = self.handle_client_recv(self.client_socket)
            if r == "退出":
                break
            # 发送一些数据到客户端
            # client_socket.send("收到 收到 ".encode('utf-8'))
        # 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
        self.client_socket.close()

    def handle_client_recv(self, client_socket):
        while True:
            # 接收对方发送过来的数据
            recv_data = client_socket.recv(1024)  # 接收 1024 个字节
            data = recv_data.decode(self.__recv_str_code)
            if data.strip():
                self.insert_to_text(data.strip())
            if data == "退出":
                return "退出"

    def close_server_connect(self):
        """"""
        if self.run_flag:
            self.insert_to_text("服务器 断开链接")
            if hasattr(self, "client_socket"):
                self.client_socket.close()
            self.tcp_server_socket.close()
            self.run_flag = False  # 标记已经断开
        else:
            self.insert_to_text("请先链接")

    def send_message(self):
        threading.Thread(target=self.send_message_thread).start()

    def send_message_thread(self):
        text = self.send_area.get(0.0, tk.END).strip()
        self.insert_to_text("(send)" + text)
        print(text)
        # 如果是字典数据
        self.client_socket.send(text.encode(self.__send_str_code))

    def open_server_socket(self):
        self.insert_to_text(f"TCP 服务器已经打开 地址:{self.port} 端口:{self.host}")
        self.create_server_socket()
        # 开启监听数据端口
        threading.Thread(target=self.listing_connect).start()
        # 绑定发送信息事件
        self.send_button.config(command=self.send_message_thread)
        # 绑定关闭连接按钮
        self.connect_button_close.config(command=self.close_server_connect)

    def open_tcp_connect(self):
        """打开tcp连接"""
        print(self.agreement_type_variable.get())
        connect_type = self.agreement_type_variable.get()
        if self.run_flag == False:
            if "TCP 服务器" == connect_type:
                self.open_server_socket()
            elif "TCP 客户端" == connect_type:
                self.open_client_socket()
            # 启动之后标记为启动成功
            self.run_flag = True
        else:
            self.insert_to_text("服务器已经启动")

    def open_client_socket(self, inet=socket.AF_INET, sock=socket.SOCK_STREAM):
        self.client_socket = socket.socket(inet, sock)
        try:
            self.client_socket.connect(self.__address)
            self.insert_to_text("服务器连接成功")
        except Exception as e:
            self.insert_to_text(str(e))

        # 处理服务器的数据接收
        threading.Thread(
            target=self.handle_client_recv, args=(self.client_socket,)
        ).start()
        # 绑定发送信息事件
        self.send_button.config(command=self.send_message_thread)
        self.connect_button_close.config(command=self.close_client)

    def close_client(self):
        self.insert_to_text("客户端断开链接")
        self.client_socket.close()


if __name__ == "__main__":
    Net = Net()
