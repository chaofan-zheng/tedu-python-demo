"""
    列表转换为字符串：
	result = "连接符".join(列表)
"""
list01 = ["a", "b", "c"]
result = "-".join(list01)
print(result)  # a-b-c

# 需求:根据某些逻辑,生成一个字符串.
# str_result = ""
# for number in range(10):
#     # 缺点:每次循环产生一个新字符串,替换之前变量,产生垃圾
#     str_result = str_result + str(number)
# print(str_result)

# 解决:用可变数据,代替不可变数据.
list_result = []
for number in range(10):
    list_result.append(str(number))
str_result = "".join(list_result)
print(str_result)
