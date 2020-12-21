"""
    列表
        删除
"""
list_name = ["邓世竹", "王杰", "崔雪松"]
# 方法1:列表名.remove(元素)
if "王杰" in list_name:
    list_name.remove("王杰")  # 如果没有报错

# 方法2:del 列表名[索引]
#      del 列表名[切片]
del list_name[-1]
del list_name[:]

# 练习4：
# 	在地区列表中删除“新疆”
# 	在新增列表中删除第1个元素
# 	在现有列表中删除前2个元素

