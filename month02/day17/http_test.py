"""
获取http请求和响应
"""
from socket import *

s = socket()
s.bind(("0.0.0.0",8000))
s.listen(5)

# 浏览器连接
c,addr = s.accept()
print("connect from",addr)

# 接收http请求
data = c.recv(1024 * 10)
print(data.decode())

# 发送响应给浏览器  \r\n
response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:text/html;charset=utf-8\r\n"
response += "\r\n" # 空行
response += "你好,世界"
c.send(response.encode())

c.close()
s.close()
