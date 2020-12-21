"""
    装饰器语法
        闭包最佳实践
            1. 有外有内：外函数接收旧功能,内函数包装新旧功能
            2. 内使用外：需要在旧功能(外部嵌套变量)基础上增加新功能
            3. 外返回内：为了客户端代码可以反复执行内部函数
        本质作用：拦截调用
"""


def new_func(func):
    def wrapper():
        print("新功能")  # 执行新功能
        func()  # 执行旧功能

    return wrapper

# func01 = new_func(func01)
# 调用new_func函数
# 将下面func01函数作为参数
# 将new_func函数的返回值给func01
@new_func
def func01():
    print("func01")

@new_func
def func02():
    print("func02")

# 旧功能 = 新功能 + 旧功能
# func01 = new_func + func01
# 执行外部函数,返回值是内部函数
# func01 = new_func(func01)
# 执行内部函数
func01()

func02()
