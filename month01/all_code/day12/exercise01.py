"""
    创建父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
    创建子类对象并画出内存图。
"""


class Car:
    def __init__(self, brand="", speed=0):
        self.brand = brand
        self.speed = speed

class ElectricCars(Car):
    def __init__(self, brand, speed, battery_capacity, charging_power=100):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


tsl = ElectricCars("特斯拉", 300, 30000, 1000)
print(tsl.brand)
print(tsl.speed)
print(tsl.battery_capacity)
print(tsl.charging_power)
