"""
    生成器应用
"""
# 需求:定义函数,计算列表中大于10的数字
list01 = [14, 5, 9, 56, 67, 67, 889]


# 传统思想:创建容器存储所有结果,缺点是占用内存过多
def func01():
    list_result = []
    for item in list01:
        if item > 10:
            list_result.append(item)
    return list_result

re = func01()
for item in re:
    print(item)


# 生成器思想：不创建容器存储结果,使用yield返回数据
def func02():
    for item in list01:
        if item > 10:
            yield item


re = func02()
for item in re:
    print(item)
