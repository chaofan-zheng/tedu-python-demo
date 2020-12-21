"""
    列表
        创建
        添加
"""
# 创建
# -- 方式1:列表名 = [元素1, 元素2, 元素3]
list_name = ["邓世竹", "王杰", "崔雪松"]
list_sex = ["男", "女", "男"]
list_age = [26, 23, 45]
#-- 方式2:列表名 = list(可迭代对象)
list01 = list("我是孙悟空")
list02 = list(range(10,31))
# 添加
# -- 追加:列表名.append(元素1)
list_name.append("于斌")
list_sex.append("女")
list_age.append(24)
print(list_name)
# -- 插入:列表名.insert(索引 ,元素)
list_name.insert(2 ,"杨德义")
print(list_name)
