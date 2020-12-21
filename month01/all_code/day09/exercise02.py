"""
	练习：定义数值累乘的函数
"""


def multiplicative(*args):
    result = 1
    for item in args:
        result *= item
    return result

print(multiplicative(1, 2))
print(multiplicative(4, 4, 5465, 6, 7))
