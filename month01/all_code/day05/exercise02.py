"""
	练习3：
        打印香港疫情信息(xx地区新增xx人现存xx人)
        将地区列表后2个元素修改为 ["XJ","SC"]
        打印地区列表元素(一行一个)
        倒序打印新增列表元素(一行一个)
"""
list_region = ["香港", "上海", "新疆"]
list_new = [15, 6, 0]
list_now = [393, 61, 49]

# 打印香港疫情信息(xx地区新增xx人现存xx人)
print("%s地区新增%d人现存%d人" % (list_region[0], list_new[0], list_now[0]))
print(f"{list_region[0]}地区新增{list_new[0]}人现存{list_now[0]}人")
# 将地区列表后2个元素修改为 ["XJ","SC"]
list_region[-2:] = ["XJ", "SC"]
print(list_region)
# 打印地区列表元素(一行一个)
for item in list_region:
    print(item)
# 倒序打印新增列表元素(一行一个)
for i in range(len(list_new) - 1, -1, -1):
    print(list_new[i])
