"""
    集合set
        价值1:去重复
"""
# 创建
# 语法1:集合名 = {元素1, 元素2, 元素3}
set_name = {"张立伟", "杨旭", "王绘杰"}
# 语法2:集合名 = set(可迭代对象)
list01 = ["a", "b", "a", "c", "a"]
set01 = set(list01)

# 添加
set_name.add("韩龙")

# 遍历
for item in set_name:
    print(item)

# 删除
set_name.discard("杨旭")  # 如果不存在也不会报错
print(set_name)
