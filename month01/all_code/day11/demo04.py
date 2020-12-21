"""
    设计思想
        分而治之 -- 划分多个类
        变则疏之 -- 寻找行为不同的变化点

    理论:
        类与类行为不同
        对象与对象数据不同
"""

# 需求:老张开车去东北
# 分析:
#    1. 识别对象:人类(老张/老李/老孙)      车类
#    2. 分配职责:   驾驶方法            行驶方法
#    3. 建立交互:
#         (1) 直接创建对象调用:老张每次去东北都使用新车
#         (2) 构造函数创建对象:老张每次开自己的车去东北
#         (3) 通过参数传递对象:老张每次用交通工具去东北
# 方式1:
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def drive(self,pos):
        print("去",pos)
        car = Car() # 创建新车
        car.run()

class Car:
    def run(self):
        print("行驶")

lz = Person("老张")
ll = Person("老李")
ls = Person("老孙")
lz.drive("东北")
lz.drive("西北")
"""

# 方式2:
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.__car = Car()  # 人的车

    def drive(self,pos):
        print("去",pos)
        self.__car.run()

class Car:
    def run(self):
        print("行驶")

lz = Person("老张") 
lz.drive("东北")
lz.drive("西北")
"""


# 方式3:
class Person:
    def __init__(self, name=""):
        self.name = name

    def drive(self, pos, vehicle):
        print("去", pos)
        vehicle.run()


class Car:
    def run(self):
        print("行驶")


lz = Person("老张")
car = Car()
lz.drive("东北", car)
