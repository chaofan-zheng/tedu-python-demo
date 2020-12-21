"""
    函数参数
        形式参数:限制实参传递方式
            默认形参:可选
            位置形参:必填
"""


# 位置形参:必填
def func02(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 默认形参:可选
# 注意:从右向左依次存在
def func01(p1="", p2=0.0, p3=0):
    print(p1)
    print(p2)
    print(p3)


# 关键字实参:按名称
func01(p2=2)
func01("a", p3=5)
