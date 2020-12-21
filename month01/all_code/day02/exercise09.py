"""
    练习：在终端中输入一个四位整数，计算每位相加和。
    例如：录入1234，打印1+2+3+4结果
    效果：
    请输入四位整数：1234
    结果是：10
"""
# # 方法1
# number = int(input("请输入四位整数:"))
# # 个位
# unit01 = number % 10
# # 十位  1234 // 10 --> 123  % 10 --> 3
# unit02 = number // 10 % 10
# # 百位  1234 // 100 --> 12 % 10  --> 2
# unit03 = number // 100 % 10
# # 千位
# unit04 = number // 1000
# result = unit01 + unit02 + unit03 + unit04
# print(result)

# 方法2
number = int(input("请输入四位整数:"))
# 个位
result = number % 10
# 十位
result += number // 10 % 10
# 百位
result += number // 100 % 10
# 千位
result += number // 1000
print(result)

