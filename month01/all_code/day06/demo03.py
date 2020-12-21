"""
    字典
        创建
        添加
"""
# list_name = ["韩龙","张立伟","杨旭"]
# list_age = [28,42,30]

# 创建
# 语法1: 字典名 = {键1:值1 , 键2:值2}
dict_han_long = {"name": "韩龙", "age": 28, "money": 10000000.5}
# 语法2:
# 可迭代对象 -格式(一分为二)-> 字典
dict01 = dict([("韩", "龙"), ("孙", "悟空"), ("齐", "天大圣")])
print(dict01)
# 添加:字典名[键]
if "sex" not in dict_han_long:
    dict_han_long["sex"] = "女"
print(dict_han_long)