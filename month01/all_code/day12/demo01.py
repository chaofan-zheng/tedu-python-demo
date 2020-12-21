"""
    继承数据
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


# 1. 子类没有构造函数,将使用父类构造函数
# class Student(Person):
#     pass

# p01 = Person("小明",22)
# s01 = Student("小明",22)

# 2. 子类存在构造函数,会覆盖父类构造函数(好像它不存在)
#    此时子类必须调用父类构造函数
class Student(Person):
    # 子类构造函数参数:父类构造函数参数 + 子类构造函数参数
    def __init__(self, name="", age=0, score=0):
        super().__init__(name, age)
        self.score = score


s02 = Student("小明", 22, 95)
print(s02.name)
print(s02.score)
