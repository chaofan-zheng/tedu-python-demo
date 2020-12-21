"""
    属性各种写法
"""

# 写法1:读写属性
"""
# 适用性:有一个实例变量,但是需要在读取和写入过程中进行限制
# 快捷键:props + 回车
class MyClass:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

m01 = MyClass(10)
print(m01.data) # 读取操作
m01.data = 20 # 写入操作
"""

# 写法2:只读属性
"""
# 快捷键:prop + 回车
# 适用性:有一个私有变量,只想提供读取功能,不希望类外修改.
class MyClass:
    def __init__(self):
        self.__data = 520
 
    @property
    def data(self):
        return self.__data

m01 = MyClass()
print(m01.data) # 读取操作
# AttributeError: can't set attribute
# m01.data = 20 # 写入操作
"""

# 写法3:只写属性
# 适用性:只需要修改实例变量,不需要读取.
# 快捷键:无
class MyClass:
    def __init__(self, data=0):
        self.data = data

    data = property()

    @data.setter
    def data(self, value):
        self.__data = value


m01 = MyClass(10)
# AttributeError: unreadable attribute
# print(m01.data) # 读取操作
m01.data = 20  # 写入操作
print(m01.__dict__)
