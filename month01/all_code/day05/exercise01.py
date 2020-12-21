"""
    练习1：
        创建地区列表、新增列表、现有列表，至少存储3行信息
    练习2：
        向以上三个列表追加数据第4行数据
        在第1个位置插入第5行数据
"""
list_region = ["香港", "上海", "新疆"]
list_new = [15, 6, 0]
list_now = [393, 61, 49]

list_region.append("四川") 
list_new.append(0)
list_now.append(27)

list_region.insert(0, "台湾")
list_new.insert(0, 0)
list_now.insert(0, 19)

print(list_region)
print(list_new)
print(list_now)
