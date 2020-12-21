"""

"""


class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 对象 --> 字符串
    def __str__(self):
        return f"我是{self.name},今年{self.age}岁了"


p01 = Person("小明", 22)
# 直接打印自定义对象,默认格式是:
# <__main__.Person object at 0x7f0d35f52e48>
print(p01)

p02 = Person("小芳", 21)
print(p02)
