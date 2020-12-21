"""
    小明使用手机打电话
    要求:增加座机,卫星电话时不影响小明.
    封装：创建人类和手机类
    继承：使用通信工具类,隔离人类与手机、座机等具体工具的变化
"""
class Communication:
    def dialing(self):
        pass

class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication):
        print(self.name, "打电话")
        # 先用
        communication.dialing()

class MobilePhone(Communication):
    # 后做
    def dialing(self):
        print("手机呼叫")

class Landline(Communication):
    def dialing(self):
        print("座机呼叫")

xm = Person("小明")
# 3. 创建子对象
xm.call(MobilePhone())
xm.call(Landline())
