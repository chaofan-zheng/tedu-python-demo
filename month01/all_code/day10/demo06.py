"""
    小结 - 实例成员与类成员
        创建
            实例变量在构造函数中:对象.变量名 = 数据
            实例方法:
                def 方法名(self):
                    pass
            类变量在类中方法外:变量名 = 数据
            类方法:
                @classmethod
                def 方法名(cls):
                    pass
        使用
            实例变量:对象.变量名
            实例方法:对象.方法名()
            类变量:类.变量名
            类方法:类.方法名()

        特殊:

"""
class MyClass:
    # 创建类变量
    data02 = 20

    # 创建类方法
    @classmethod
    def func02(cls):
        print(cls.data02)

    def __init__(self):
        # 创建实例变量
        self.data01 = 10

    # 创建实例方法
    def func01(self):
        print(self.data01)

m01 = MyClass()
# 操作实例变量
print(m01.data01)
# 操作类变量
print(MyClass.data02)
# 通过对象访问实例方法
m01.func01()
# 不建议通过类名访问
# MyClass.func01(m01)

# 通过类访问类方法
MyClass.func02()
# 不建议通过对象访问类方法
# m01.func02()



