"""
    总结Python语言所有变量
"""
# 1. 全局变量:整个文件可用
data01 = 10


def func01():
    # 2. 局部变量:当前函数内部可用
    data02 = 20


class MyClass:
    # 4. 类变量:通过类名访问
    data04 = 40

    def __init__(self):
        # 3. 实例变量:通过对象访问
        self.data03 = 30


m01 = MyClass()
print(m01.data03)
