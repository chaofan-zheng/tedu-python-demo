"""
    字典
        定位
        遍历
"""
dict_han_long = {
    "name": "韩龙",
    "age": 28,
    "money": 10000000.5
}
# 定位:字典名[键]
print(dict_han_long["name"])
# 如果存在键则修改
if "name" in dict_han_long:
    dict_han_long["name"] = "龙龙"
print(dict_han_long)

# 遍历
# -- 获取每个键
for key in dict_han_long:
    print(key)
# -- 获取每个值
for value in dict_han_long.values():
    print(value)
# -- 获取每个键和值
# item -> (键,值)
# for item in dict_han_long.items():
#     print(item)
for k,v in dict_han_long.items():
    print(k)
    print(v)