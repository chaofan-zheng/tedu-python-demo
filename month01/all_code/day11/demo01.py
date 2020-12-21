"""
    属性原理
        1. 创建类变量与实例变量名称相同
        2. 创建属性对象同时绑定读取方法
        3. 再绑定写入方法
"""


class Wife:
    def __init__(self, age=0):
        self.age = age  # 调用set_age方法

    # 负责读取
    def get_age(self):
        return self.__age

    # 负责写入
    def set_age(self, value):
        self.__age = value

    # 创建类变量关联 属性对象(具有读取方法)
    age = property(get_age)
    # 使用类变量关联 具有写入函数的新属性对象(读+写)
    age = age.setter(set_age)


w01 = Wife(26)
# 读取数据 自动调用 get_age方法
w01.age = 26
print(w01.age)
# 属性可以将方法变为像操作变量一样方便
w01.set_age(26)
print(w01.get_age())
