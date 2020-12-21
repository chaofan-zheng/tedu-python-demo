"""
    列表
        定位
        遍历
"""
# 1. 定位(读取/修改)
list_name = ["邓世竹", "王杰", "崔雪松"]
# -- 索引: 列表名[整数]
print(list_name[0])
list_name[0] = "小竹竹"
print(list_name)
# -- 切片: 列表名[开始:结束:间隔]
print(list_name[-2:])  # 原理:创建新容器
list_name[-2:] = ["老王", "雪松"]
print(list_name)

# 2. 遍历
# 从头到尾读取元素
for item in list_name:
    print(item)

# 非从头到尾读取元素
# 修改
# for i in range(len(list_name)):# 0 1 2
#     list_name[i] = ""

# 非从尾到头
# len(list_name) - 1 : 从最大索引开始
# -1 : 不会包含-1,实际包含的是0
# -1 : 倒序
for item in range(len(list_name) - 1, -1, -1):  # 2 1 0
    print(item)
