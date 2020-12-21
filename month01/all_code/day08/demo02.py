"""
    返回值语法
        return 可以返回后面的结果
        Python语言,函数没有返回值,默认返回None
        return 还可以退出函数(无视循环)
"""

# return 可以返回后面的结果
def func01():
    print("func01执行了")
    return "ok"

data01 = func01()
print(data01)

# Python语言,函数没有返回值,默认返回None
def func02():
    print("func02执行了")

data02 = func02() # None
print(data02)

# return 还可以退出函数(无视循环)
def func03():
    print("func02执行了")
    while True:
        while True:
            while True:
                return
    print("func02又执行了")

data03 = func03() # None
print(data03)





