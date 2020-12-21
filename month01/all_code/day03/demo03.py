"""
    逻辑运算符：判断两个命题关系的符号
        与 或 非
        短路逻辑:尽量将耗时的条件,放在后面.
"""
# 有钱
# print(int(input("请输入您的财产：")) > 100000000)
# 有房
# print(int(input("请输入您的房产数量：")) > 0)

# 与：一假俱假   条件都满足,结果才成立  表达并且关系
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# 有钱 还得 有房
# 与逻辑的短路：第一个条件不满足,第二个条件不再判断
print(int(input("请输入您的财产：")) > 100000000 and int(input("请输入您的房产数量：")) > 0)
