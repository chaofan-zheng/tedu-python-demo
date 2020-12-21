# 练习1：将列表中所有奇数设置为None
list01 = [4, 5, 6, 67, 8]
# for i, item in enumerate(list01):
#     if item % 2:
#         list01[i] = None
#
# print(list01)

# 练习2：将列表中所有偶数自增
for i, item in enumerate(list01):
    if item % 2 == 0:
        list01[i] += 1

print(list01)
