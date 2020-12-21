"""
    函数式编程语法
        理论支柱:能够将函数赋值给变量
"""
def func01():
    print("func01执行了")

# 注意注意注意:写完函数不要写小括号,才是将函数赋值给变量
#           否则就是将函数返回值给变量
a = func01
func01() # 直接调用
a() # 间接调用


# 简述函数式编程优点
# 将函数作为参数,就意味着将行为(逻辑/条件)传入到函数中
def func02():
    print("func02执行了")


def func03(func):
    print("func03执行了")
    # func02() # 直接调用 (绑死了func03 -- func02)
    func() # 间接调用(与传入的实际参数绑定)

func03(func02) # func03 -- func02
func03(func01) # func03 -- func01


