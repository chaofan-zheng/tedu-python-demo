"""
    类型转换
        语法：
            结果 = 目标类型(待转数据)
        适用性：
            获取数据: 字 --> 数
            显示结果: 数 --> 字
    练习:exercise05

"""
# input函数的结果一定是字符串类型str
age = int(input("请输入年龄：")) + 1
print("明年" + str(age) + "岁了")

# 1. str  <-->  int
data01 = int("18")
data02 = str(18)

# 2. str  <-->  float
data03 = float("18.6")
data04 = str(18.6)

# 3. float  <-->  int
data05 = int(18.9)  # 18 向下取整
data06 = float(18)  # 18.0
print(data06)

# 4. 注意
# 由字符串类型转换为其他类型,字符串的格式必须符合目标类型要求.
# data07 = int("100+")
# data07 = int("100.5")
# data08 = float("100.5abc")
data08 = float("100")
print(data08)
