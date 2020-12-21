"""
    练习：
        创建子类：狗(跑)，鸟类(飞)
        创建父类：动物(吃)
        体会子类复用父类方法
          体会 isinstance、issubclass与type的作用.
"""


# 从思想层面讲:先有子再有父,从子 -泛化-> 到父
# 从编码层面讲:先有父再有子,从父 -特化-> 到子

class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        print("跑")


class Bird(Animal):
    def fly(self):
        print("飞")


a01 = Animal()
a01.eat()

d02 = Dog()
d02.eat()

print(isinstance(d02, Animal))
print(issubclass(Dog, Animal))
print(type(d02) == Dog)
