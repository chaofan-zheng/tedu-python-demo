"""
    容器　－　总结
        1. 种类与特点
            字符串：存储字符编码值,不可变,序列
            列表：存储变量,可变,序列
            元组：存储变量,不可变,序列
            字典：存储键值对,可变,散列
                键：必须唯一且不可变数据(数字,bool,字符串,元组)
            集合：存储键,可变,散列

        2. 不可变与可变:
            在内存中所有的数据都可以视为不可变数据,
            为了开发更加方便,创建了可变数据.
            可变:预留空间 + 自动扩容
            不可变:按需分配

        3. 序列与散列:
            序列:有顺序,存储空间连续(节省内存),通过索引切片定位(定位灵活)
            散列:无顺序,存储空间分散(定位迅速),通过键定位
"""
# 1. 创建
list01 = [10, 20, 30]
dict01 = {"a": 10, "b": 20, "c": 30}
# 2. 添加
list01.append(40)
list01.insert(1, 50)
dict01["d"] = 40

# 3. 定位
print(list01[0])
# 原理:通过切片读取数据,会创建新容器
print(list01[:2])
# 原理:通过切片修改数据,会遍历右侧可迭代对象,依次存入左侧定位区域
list01[:2] = "悟空"

print(dict01["d"])
dict01["d"] = 40

# 4. 遍历
# 从头到尾读取数据
for item in list01:
    print(item)
# 非从头到尾读取数据
for i in range(len(list01) - 1, -1, -1):
    print(list01[i])

for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for k, v in dict01.items():
    print(k)
    print(v)

# 5. 删除
list01.remove(10)
del list01[0]
del list01[-2:]

del dict01["a"]
