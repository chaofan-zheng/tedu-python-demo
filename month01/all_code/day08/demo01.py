"""
    函数设计理念
        崇尚小而精,拒绝大而全

    返回值
        函数定义者给函数调用者传递的信息
"""


# 需求:创建两个数字相加的函数

# 大而全(从头到尾实现功能)
# def add():
#     number_one = int(input("请输入第一个数字:"))
#     number_two = int(input("请输入第二个数字:"))
#     result = number_one + number_two
#     print("结果是:" + str(result))

# add()

def add(number_one, number_two):
    """
        两个数字相加
    :param number_one:第一个数字
    :param number_two:第二个数字
    :return:相加后的结果
    """
    result = number_one + number_two
    return result  # 返回 数据


number_one = int(input("请输入第一个数字:"))
number_two = int(input("请输入第二个数字:"))
res = add(number_one, number_two)
print("结果是:" + str(res))
