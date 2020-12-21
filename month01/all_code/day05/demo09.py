"""
    列表推导式
        列表名 = [对变量操作 for 变量 in 可迭代对象 if 条件]
        适用性:
            根据可迭代对象,构建列表
"""

list01 = [54, 5, 65, 67, 7, 78, 89]
# list02 = []
# for item in list01:
#     if item > 10:
#         list02.append(item)
list02 = [item for item in list01 if item > 10]
print(list02)
