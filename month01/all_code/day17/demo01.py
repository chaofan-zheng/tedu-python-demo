"""
    内置生成器
        enumerate : 获取元素的同时获取索引
        价值：读取元素同时可以修改元素
"""
list01 = [65, 67, 78, 9, 76, 443, 4, 7]
# 需求:将列表中大于10的元素修改为10
"""
# 从头到尾读取数据
for item in list01:
    if item > 10:
        item = 10  # 修改变量item,与列表无关

for i in range(len(list01)):
    if list01[i] > 10:
        list01[i] = 10  # 通过索引定位元素再修改

print(list01)
"""

# 　(索引,元素)
# for item in enumerate(list01):
#     print(item)

# for i,element in enumerate(list01):
#     print(i,element)

for i, element in enumerate(list01):
    if element > 10:
        list01[i] = 10
# print(list01)

# 快捷键：
# for .. in 快捷键：　iter + 回车
# for .. in  enumerate 快捷键：　itere + 回车
