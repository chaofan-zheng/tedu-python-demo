"""
    常用算法
        变量交换
        计算最值
        排序
"""
"""
复习
# 变量交换
a = 10
b = 20
# 先构建元组,再拆包
a, b = b, a

data = [6, 5, 76, 5, 5, 76, 87, 9]
min_value = data[0]
for i in range(1,len(data)):
    if min_value > data[i]:
        min_value = data[i]
print(min_value)
"""

# 升序(小 --> 大)
# 保障第1个位置就是最小值(与后面比较,发现更小则交换)
list01 = [55, 65, 67, 76, 8, 6, 9, 64]
"""
# 保障第1个位置就是最小值(与后面比较,发现更小则交换)
for i in range(1, len(list01)):
    if list01[0] > list01[i]:
        list01[0], list01[i]=list01[i],list01[0]
# 保障第2个位置就是最小值(与后面比较,发现更小则交换)
for i in range(2, len(list01)):
    if list01[1] > list01[i]:
        list01[1], list01[i]=list01[i],list01[1]
"""
# 取数据
for r in range(len(list01) - 1):  # 0     1     2
    # 作比较
    for c in range(r + 1, len(list01)):  # 1~7  2~7  3~7
        # 如果发现更小
        if list01[r] > list01[c]:
            # 则交换
            list01[r], list01[c] = list01[c], list01[r]
print(list01)

