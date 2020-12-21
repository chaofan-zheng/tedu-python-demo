"""
    继承
        财产:钱孩子不用挣,但是可以用
        皇位:江山不用孩子打,但是可以坐
        编程:代码不用子类写,但是可以调
"""


class Person:
    def say(self):
        print("说话")

class Student(Person):
    def study(self):
        print("学习")
        self.say()

class Teahcer(Person):
    def teach(self):
        print("教学")


# 创建子类对象,可以访问父类成员和子类成员
t01 = Teahcer()
t01.teach()
t01.say()

# 创建父类对象,只能访问父类成员
p02 = Person()
p02.say()

#  判断一个对象　与　另外一个类型的关系
# 老师对象是一种老师类型
print(isinstance(t01, Teahcer))  # True
# 老师对象是一种人类型
print(isinstance(t01, Person))  # True
# 老师对象是一种学生类型
print(isinstance(t01, Student))  # False
# 人对象是一种学生类型
print(isinstance(p02, Student))  # False

# 老师类型是一种老师类型
print(issubclass(Teahcer, Teahcer))  # True
# 老师类型是一种人类型
print(issubclass(Teahcer, Person))  # True
# 老师类型是一种学生类型
print(issubclass(Teahcer, Student))  # False
# 人类型是一种学生类型
print(issubclass(Person, Student))  # False

# 老师对象是老师类型
print(type(t01) == Teahcer)  # True
# 老师对象是人类型
print(type(t01) == Person)  # False
# 老师对象是学生类型
print(type(t01) == Student)  # False
# 人对象是学生类型
print(type(p02) == Student)  # False