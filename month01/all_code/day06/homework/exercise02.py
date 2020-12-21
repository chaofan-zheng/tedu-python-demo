"""
    2. 将列表中的数字累乘
        list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    结果：806400
"""
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
result = 1  # 因为1乘以任何数字,都不改变.
for item in list02:
    result *= item
print(result)
