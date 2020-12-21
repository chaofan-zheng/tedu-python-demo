"""
    列表推导式
    生成器表达式
    传统思想与生成器思想的选择策略
        传统思想:创建容器存储所有结果
            优点:操作数据灵活(支持索引切片,反复使用)
            缺点:占用内存过多
        生成器思想:动态返回所有结果
            优点:几乎不占内存
            缺点:操作数据不灵活(不支持索引切片,只能用一次)
            解决方案:
                容器名(生成器)
        策略:
            当做功能的程序员需要提供多个数据时,优先选择生成器.
            但是,使用功能的程序员如果不能接受生成器缺点,可以自行转换为容器
"""
list01 = [54, 5, 65, 67, 7, 78, 89]
# list02 = []
# for item in list01:
#     if item > 10:
#         list02.append(item)
# 传统思想:容器存储所有结果
list02 = [item for item in list01 if item > 10]
print(list02[-1])
print(list02[-2:])
for item in list02:
    print(item)
for item in list02:
    print(item)

# 生成器思想:循环一次计算一次返回一次
datas = (item for item in list01 if item > 10)

tuple_data = tuple(datas)
print(tuple_data[-1])
