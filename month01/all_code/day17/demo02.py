"""
    内置生成器
        zip:同时从多个可迭代对象中取出对应元素,形成元组
"""
list01 = [1, 2, 3, 4]
list02 = [5, 6, 7, 8]

for item in zip(list01, list02):
    print(item)

map = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# for item in zip(map[0],map[1],map[2],map[3]):
# 将map拆分成多个实参，传递给zip(当map行变化,不用修改代码)
# new_map = []
# for item in zip(*map):
#     new_map.append(list(item))
# print(new_map)
new_map = [list(item) for item in zip(*map)]
print(new_map)
