"""
    属性
"""


class Wife:
    def __init__(self,age=0):
        self.age = age

    # 使用函数名关联 属性对象(具有读取方法)
    @property  # age = property(读取方法)
    def age(self):# 读取方法
        return self.__age

    # 使用函数名关联 具有写入方法的新属性对象(读+写)
    # age = age.setter(写入方法)
    @age.setter
    def age(self, value):# 写入方法
        if 20 <= value <= 100:
            self.__age = value
        else:
            raise Exception("我不要")


shuang_er = Wife(30)
print(shuang_er.age)
