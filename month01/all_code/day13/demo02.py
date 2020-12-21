"""
   多态3步骤
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def drive(self, pos, vehicle):
        print("去", pos)
        # 1. 调用父(交通工具)
        vehicle.transport()

class Vehicle:
    def transport(self):
        pass

class Car(Vehicle):
    # 2. 子重写 (按照人调用交通工具的方式干活)
    def transport(self):
        print("行驶")

class Airplane(Vehicle):
    def transport(self):
        print("飞行")

lz = Person("老张")
car = Car()
air = Airplane()
# 3. 创建子  选择以汽车方式去东北
lz.drive("东北", car)
