"""
练习3：根据下列代码，创建降序排列函数。
list01 = [5, 15, 25, 35, 1, 2]
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
"""


def desecending_order(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]


list01 = [5, 15, 25, 35, 1, 2]
desecending_order(list01)  # 不用变量接收返回值
print(list01)  # 通过传入的可变对象,获取函数修改结果
