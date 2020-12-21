"""
    练习:降序(大 --> 小)
"""
list01 = [55, 65, 67, 76, 8, 6, 9, 64]
# 取数据
for r in range(len(list01) - 1):
    # 作比较
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]