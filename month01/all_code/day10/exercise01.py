"""
    练习1：创建狗类
    数据：品种、昵称、身长、体重
        行为：吃(体重增长1)
        实例化两个对象并调用其函数
        画出内存图
"""
class Dog:
    def __init__(self, species="", pet_name="", height=0, weight=0):
        self.species = species
        self.pet_name = pet_name
        self.height = height
        self.weight = weight

    def eat(self):
        print("吃")
        self.weight += 1

mx = Dog("拉布拉多", "米咻", 40, 80)
mx.eat()
print(mx.weight)
hm = Dog("哈士奇", "黑米", 43, 82)
hm.eat()
print(hm.weight)