"""
练习4：
	在地区列表中删除“新疆”
	在新增列表中删除第1个元素
	在现有列表中删除前2个元素
"""
list_region = ["香港", "上海", "新疆"]
list_new = [15, 6, 0]
list_now = [393, 61, 49]

list_region.remove("新疆")
del list_new[0]
del list_now[:2]

print(list_region)
print(list_new)
print(list_now)
