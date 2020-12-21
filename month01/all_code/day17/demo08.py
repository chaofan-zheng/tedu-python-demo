"""
    lambda应用
"""
from common.iterable_tools import IterableHelper

list01 = [63, 5, 56, 7, 8, 9]


def condtion01(number):
    return number < 10


# lambda number:number < 10

#  查找能被5整除的数字
def condition02(item):
    return item % 5 == 0

for item in IterableHelper.find_all(list01, lambda number: number < 10):
    print(item)

for item in IterableHelper.find_all(list01, lambda item:item % 5 ==0):
    print(item)
