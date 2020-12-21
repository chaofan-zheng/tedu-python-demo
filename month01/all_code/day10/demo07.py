"""
    私有成员
        做法:命名以双下划线开头
        作用:在类外无法访问
        本质:障眼法(看见的不是实际的)
            看见的是双下划线命名的变量__data
            实际是单下划线+类名+私有变量名_MyClass__data
"""

class MyClass:
    def __init__(self):
        self.__data = 10

    def __func01(self):
        print("func01执行了")

m01 = MyClass()
# print(m01.__data)
# print(m01._MyClass__data)

# m01.__func01()
# m01._MyClass__func01()