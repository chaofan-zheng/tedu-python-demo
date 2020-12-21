"""
    需求:老张开车去东北
    变化:飞机/轮船/骑车....
    思想:
        封装:将需求分解为多个类
            人类   汽车   飞机   轮船  自行车 ...
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def drive(self, pos, vehicle):
        print("去", pos)
        vehicle.transport()

class Vehicle:
    def transport(self):
        pass

class Car(Vehicle):

    def transport(self):
        super().transport()
        print("行驶")


class Airplane(Vehicle):
    # 重写快捷键:ctrl + o
    def transport(self):
        print("飞行")

lz = Person("老张")
car = Car()
air = Airplane()
lz.drive("东北", car)
