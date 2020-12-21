"""
    属性
        价值:保障数据在有效范围内
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 100:
            self.__age = value
        else:
            raise Exception("我不要")


shuang_er = Wife("双儿", 30)
print(shuang_er.age)
print(shuang_er.__dict__)
