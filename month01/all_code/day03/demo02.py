"""
    字面值(各种写法)
"""
# 1. 整数int字面值
# 十进制：每位用十种状态计数，逢十进一，写法是0~9。
number01 = 10
# 二进制：每位用二种状态计数，逢二进一，写法是01。
number02 = 0b10
# 八进制：每位用八种状态计数，逢八进一，写法是0~7。
number03 = 0o10
# 十六进制：每位用十六种状态计数，逢十六进一，写法是0~9  a(10)~f(15)。
number04 = 0x10
print(number04)

# 2. 浮点型float字面值
# 小数
number05 =0.00003
# 科学计数法(当小数0大于4个时,建议使用)
print(number05)# 3e-05


