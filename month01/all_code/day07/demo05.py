"""
    函数
"""
# 缺点:代码重复 = 万恶之源

"""
# 做法(变化) + 用法
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
# ......
# 做法(变化)  + 用法
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
"""


# 创建函数 - 做法(变化)
def attack():
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")
    print("侧踹")

# 调用函数 - 用法
attack() #  如果需要查看函数内部执行步骤,使用F7
attack()
