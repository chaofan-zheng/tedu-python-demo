"""
    装饰器语法 - 细节
         内部函数返回值：旧功能返回值
         内部函数参数：多个实参 合为 一个元组
         内部函数调用旧功能时：一个元组 拆为 多个形参
"""


# 拦截
def new_func(func):
    def wrapper(*args,**kwargs): # 多个实参 合为 一个元组
        print("新功能")
        res = func(*args,**kwargs) # 一个元组 拆为 多个形参
        return res  # 内部函数返回值：旧功能返回值

    return wrapper


@new_func
def func01(p1):
    print("func01", p1)
    return 100

@new_func
def func02(p1, p2):
    print("func02", p1, p2)
    return 200

print(func01("a"))
print(func02("a", "b"))
print(func02("a", p2 = "b"))
