import socket

# 创建socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 本地信息
address = ('192.168.0.7', 7788)

# 绑定
tcp_server_socket.bind(address)

tcp_server_socket.listen(128)

while True:
    # 等待新的客户端连接
    client_socket, clientAddr = tcp_server_socket.accept()
    while True:
        # 接收对方发送过来的数据
        recv_data = client_socket.recv(1024)  # 接收1024个字节
        if recv_data:
            print('接收到的数据为:', recv_data.decode('gbk'))
        else:
            break
    client_socket.close()

tcp_server_socket.close()