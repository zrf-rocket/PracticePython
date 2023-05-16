from __init__ import WEIXIN_URL, CSDN_URL
# with语句的使用示例

# 处理文件资源
with open("__init__.py", "r") as f:
    data = f.read()
    print(data)


# 处理网络连接资源
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('www.baidu.com', 80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n")
    data = s.recv(1024)
    print(data)