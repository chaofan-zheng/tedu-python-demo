"""
   Enclosing  外部嵌套作用域 ：函数嵌套。
"""


def func01():
    # 局部变量：相对于文件
    # 外部嵌套变量:相对于内函数
    a = 10

    def func02():
        # 读取外部嵌套变量
        print(a)

    func02()


func01()


def func03():
    a = 10

    def func04():
        # 不能修改外部嵌套变量
        # 如果修改,必须通过nonlocal声明
        nonlocal a
        a = 20

    func04()
    print(a)


func03()
