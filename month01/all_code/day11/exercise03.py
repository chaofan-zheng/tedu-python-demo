"""
    练习1：以面向对象思想,描述下列情景.
    小明请保洁打扫卫生
    要求:写出3种交互方式
"""
# 方式1:小明每次通知新保洁
"""
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self):
        print("通知")
        cleaner = Cleaner()
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Client("小明")
xm.notify()
"""

# 方式2:小明每次通知自己的保洁
"""
class Client:
    def __init__(self, name=""):
        self.name = name
        # 实例变量/私有变量
        self.__cleaner = Cleaner()

    def notify(self):
        print("通知")
        self.__cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Client("小明")
xm.notify()
"""

# 方式3:小明每次通知传入的参数(家政服务)
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self,cleaner):
        print("通知")
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Client("小明")
cleaner = Cleaner()
xm.notify(cleaner)