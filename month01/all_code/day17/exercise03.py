# 练习1：使用生成器表达式在列表中获取所有字符串.
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
# 制作生成器
datas = (item for item in list01 if type(item) == str)
# 使用生成器
for item in datas:
    print(item)

# 练习2：在列表中获取所有整数,并计算它的平方.
# 制作生成器
datas = (item **2 for item in list01 if type(item) == int)
# 使用生成器
list_data = list(datas)
print(list01[0])
print(list01[-2:])
