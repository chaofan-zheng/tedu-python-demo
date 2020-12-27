"""
客户端请求操作 --》 2个界面
"""
from socket import *
import sys

ADDR = ("127.0.0.1", 8880)


# 发起请求
class DictRequest:
    def __init__(self):
        self.sock = self.create_socket()

    def create_socket(self):
        sock = socket()
        sock.connect(ADDR)
        return sock

    def do_register(self):
        while True:
            name = input("Name:")
            passwd = input("Password:")

            if " " in name or " " in passwd:
                print("用户名或密码不能有空格")
                continue
            # 发送请求
            msg = "R %s %s" % (name, passwd)
            self.sock.send(msg.encode())
            # 等待响应
            result = self.sock.recv(128)
            if result == b'OK':
                print("注册成功")
            else:
                print("注册失败")
            return

    def do_login(self):
        name = input("Name:")
        passwd = input("Password:")

        # 发送请求
        msg = "L %s %s" % (name, passwd)
        self.sock.send(msg.encode())
        # 等待响应
        result = self.sock.recv(128)
        if result == b'OK':
            print("登录成功")
            return name
        else:
            print("登录失败")

    def do_exit(self):
        self.sock.send(b"E")

    def do_query(self, name):
        while True:
            word = input("单词：")
            if word == '##':
                break
            msg = "Q %s %s" % (name, word)
            self.sock.send(msg.encode())
            # 无论是否查到都打印返回结果
            data = self.sock.recv(1024 * 10)
            print(data.decode())

    def do_hist(self, name):
        msg = "H " + name
        self.sock.send(msg.encode())
        # 不能确定接收几次
        while True:
            data = self.sock.recv(1024).decode()
            if data == "##":
                break
            print(data)


class DictView:
    def __init__(self):
        self.request = DictRequest()

    def login_menu(self, name):
        while True:
            print("""
    ================ Query ===============
     1. 查询单词   2. 历史记录    3. 注销
    ======================== User: %s ==
            """ % name)
            item = input("请输入选项:")
            if item == '1':
                self.request.do_query(name)
            elif item == '2':
                self.request.do_hist(name)
            elif item == '3':
                break
            else:
                print("请输入正确选项！")

    def __display_menu(self):
        print("""
    ============= Welcome =============
      1. 登录     2. 注册      3. 退出
    ===================================
        """)

    def __select_menu(self):
        item = input("请输入选项:")
        if item == '1':
            name = self.request.do_login()
            if name:
                self.login_menu(name)
        elif item == '2':
            self.request.do_register()
        elif item == '3':
            self.request.do_exit()
            sys.exit("谢谢使用")
        else:
            print("请输入正确选项！")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


if __name__ == '__main__':
    view = DictView()
    view.main()
