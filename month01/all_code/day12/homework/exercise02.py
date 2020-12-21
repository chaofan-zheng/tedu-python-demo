"""
    需求：小明使用手机打电话
    划分原则:
        数据不同使用对象区分 -- 小王/小孙...
        行为不同使用类区分 -- 手机/卫星电话...

    识别对象：
            人类        手机
    分配职责：
            打电话      通话
    建立交互：
           人类  调用  手机
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication):
        print(self.name, "打电话")
        communication.dialing()


class MobilePhone:
    def dialing(self):
        print("呼叫")


xm = Person("小明")
xm.call(MobilePhone())
