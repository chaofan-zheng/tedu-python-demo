"""
使用http协议
将一个文件的内容作为响应体发送给浏览器显示
（文件可以是文本也可以是图片）
Content-Type:image/jpeg   图片
Content-Type:text/plain  文本
"""

from socket import *

# 处理浏览器请求
def http_handle(c):
    # 接收http请求
    data = c.recv(1024 * 10)
    print(data.decode())

    # 发送响应给浏览器  \r\n
    with open("timg.jpeg",'rb') as f:
        data = f.read()
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:image/jpg\r\n"
        response += "Content-Length:%s\r\n"%len(data)
        response += "\r\n"  # 空行
        response = response.encode() + data
    c.send(response)

def main():
    s = socket()
    s.bind(("0.0.0.0",8001))
    s.listen(5)

    # 浏览器连接
    c,addr = s.accept()
    print("connect from",addr)
    # 接收请求发送响应
    http_handle(c)
    c.close()
    s.close()

if __name__ == '__main__':
    main()