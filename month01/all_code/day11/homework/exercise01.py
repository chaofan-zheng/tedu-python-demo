"""
    画出下列代码内存图
    找出打印结果
"""
g01 = 100
g02 = 100
g03 = [100]

def func01():
    g01 = 200# 创建一个局部变量

def func02():
    global g02
    g02 = 200

def func03():
    g03[0] = 200 # 读取全局变量,修改列表元素

func01()
print(g01)  # 100
func02()
print(g02)  # 200
func03()
print(g03) # [200]

class MyClass:
    cls01 = 300 # 饮水机

    def __init__(self):
        self.ins01 = 400 # 杯子

        self.ins01 += 1
        MyClass.cls01 += 1


instance01 = MyClass()# 400->401  300 -> 301
print(instance01.ins01)  # 401
print(MyClass.cls01)  # 301

instance02 = MyClass()# 400->401  301 -> 302
print(instance02.ins01)  # 401
print(MyClass.cls01)  # 302
