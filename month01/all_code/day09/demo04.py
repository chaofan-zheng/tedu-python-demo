"""
    函数参数
        形式参数
            命名关键字形参
"""


# 命名关键字形参:星号后面的形参(p1,p2)
# 必须使用关键字实参
def func01(*args, p1, p2):
    print(args)
    print(p1)
    print(p2)


func01(p1=1, p2=2)


# TypeError: func01() missing 1 required keyword-only argument: 'p1'
# func01(1, 2, 3,p2=2)

# p1是位置形参,p2是命名关键字形参
def func02(p1, *, p2=0):
    print(p1)
    print(p2)


func02(1)
# 分清实参主(位置形参)次(命名关键字形参)
func02(1, p2=2)

# 应用:
# 　def print(*values,sep = " ",end = "\n")
print()  # 换行
print("悟空", 100, 1.5)  # 直接打印多个不同类型数据
print("悟空", 100, 1.5, sep="-")  # 悟空-100-1.5
print("悟空", 100, sep="-", end=" ")
# print("悟空", 100, "-", " ")
