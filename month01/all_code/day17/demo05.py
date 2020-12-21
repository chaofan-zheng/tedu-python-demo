"""
    函数式编程思想
"""
list01 = [63, 5, 56, 7, 8, 9]

# 多个功能,主体结构相同,核心算法不同.
# 分:将不同的代码定义到函数中,将相同的代码也定义到函数中
# 隔:使用参数,隔离相同代码的函数与不同代码的函数
# 做:使用lambda函数,定义不同的代码
def find01():
    for number in list01:
        if number < 10:
            yield number

def find02():
    for number in list01:
        if number % 3 ==0:
            yield number

for item in find02():
    print(item)

# 后做
# 变化点(火车/汽车/....)
def condtion01(number):
    return number < 10

def condtion02(number):
    return number % 3 ==0

# 客户端代码(老张)
def find(func): # 参数func(交通工具)
    for number in list01:
        # if number % 3 ==0:
        # if condtion02(number):
        # 先确定用法(1参数与bool返回值)
        if func(number):
            yield number

for item in find(condtion01):
    print(item)