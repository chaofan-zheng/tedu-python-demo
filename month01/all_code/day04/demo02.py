"""
    for  +  range
        range 能够产生一个范围内的整数
"""
# 写法1: range(开始,结束,间隔)
# 注意:不包含结束值
for item in range(3, 6, 1):
    print(item)  # 3 4 5

# 写法2: range(开始,结束)
# 注意:间隔默认1
for item in range(3, 6):
    print(item)  # 3 4 5

# 写法3: range(开始,结束)
# 注意:开始默认0
for item in range(6):
    print(item)  # 0 1 2 3 4 5

# 练习：
# 在终端中累加 0  1  2  3
# 在终端中累加 2  3  4  5  6
# 在终端中累加 1  3  5  7
# 在终端中累加 8  7  6  5  4
# 在终端中累加 -1  -2  -3  -4  -5