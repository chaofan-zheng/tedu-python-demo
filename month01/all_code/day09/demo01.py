"""
    函数参数
        实际参数:与形参进行对应
            位置实参:按顺序
            关键字实参:按名称
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

# 位置实参:按照顺序与形参进行对应
func01(1, 2, 3)
# 关键字实参:按照名称与形参进行对应
func01(p2=2, p1=1, p3=3)
func01(p2=2, p3=3, p1=1)

# TypeError: func01() missing 1 required positional argument: 'p3'
# func01(1, 2)# 缺少p3

# TypeError: func01() takes 3 positional arguments but 4 were given
# func01(1, 2, 3, 4) # 需要3个参数但是给了4个
