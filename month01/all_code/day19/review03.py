"""
    复习 - 面向对象
        实例成员
        类成员
        静态方法
        属性:保护实例变量在有效范围内
"""
data02 = 20


class MyClass:
    # 类变量：大家相同的数据
    data02 = 20

    # 类方法：操作类变量
    @classmethod
    def func02(cls):
        cls.data02 += 1

    def __init__(self, data01=0):
        # 实例变量：对象不同的数据
        self.data01 = data01

    # 实例方法：操作实例变量
    def func01(self):
        self.data01 += 1

    # 静态方法：不能操作其他成员,用于完成工具(独立强且常用)函数
    # 在集成操作框架中所有对可迭代对象的操作,都是静态函数
    @staticmethod
    def func03():
        pass


m01 = MyClass(100)
# 通过对象访问实例成员
m01.func01()
print(m01.data01)

# 因为要保护实例变量的读写过程,所以使用属性
class MyClass:
    def __init__(self, data01=0):
        self.data01 = data01
        self.__data02 = 100

    # 读写属性
    @property  # data01 = property(data01)
               # 属性名 = property(读取函数)
    def data01(self):# 读取函数
        return self.__data01

    @data01.setter # data01 = data01.setter(data01)
                   # 属性名 = data01.setter(写入函数)
    def data01(self, value): # 写入函数
        self.__data01 = value

    # 只读属性
    @property
    def data02(self):
        return self.__data02

m02 = MyClass(1)
print(m02.data01)
print(m02.data02)