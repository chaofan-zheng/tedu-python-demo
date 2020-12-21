"""
    练习4：创建函数,计算梯形面积.
        top_base = float(input("请输入上底："))
        bottom_base = float(input("请输入下底："))
        height = float(input("请输入高："))
        result = (top_base + bottom_base) * height / 2
        print("梯形面积是：" + str(result))
"""


def calculate_trapezoid_area(top_base, bottom_base, height):
    """

    :param top_base:
    :param bottom_base:
    :param height:
    :return:
    """
    # result = (top_base + bottom_base) * height / 2
    # return result
    return (top_base + bottom_base) * height / 2

print(calculate_trapezoid_area(2, 3, 4))
