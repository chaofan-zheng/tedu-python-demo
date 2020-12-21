"""
    函数参数
        实参参数
            序列实参:拆
        形式参数
            星号元组实参:合
"""
def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


list01 = [1, 2, 3]
tuple01 = ("a", "b", "c")
str01 = "孙悟空"
# 序列实参:将一个序列 拆分为 多个实参,按顺序对应
# 适用性:需要在其他环境中构建实参
func01(*list01)


# 星号元组形参:将多个位置实参 合并为 一个元组
# 适用性:需要位置实参数量无限
def func02(*args):
    print(args)


func02()
func02(1)
func02(1, 2, 3)
func02(*list01)
func02(*str01)
