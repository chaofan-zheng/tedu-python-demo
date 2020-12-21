"""
    需求:老张开车去东北
    变化:飞机/轮船/骑车....
    思想:
        封装:将需求分解为多个类
            人类   汽车   飞机   轮船  自行车 ...
    缺点:
        违背面向对象设计原则 - 开闭原则
            允许增加新功能(飞机),不能修改之前的代码(人类).
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def drive(self, pos, vehicle):
        print("去", pos)
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("行驶")

class Airplane:
    def fly(self):
        print("飞行")

lz = Person("老张")
car = Car()
air = Airplane()
lz.drive("东北", car)
