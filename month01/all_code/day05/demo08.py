"""
    字符串转换为列表：
    列表 = “a-b-c-d”.split(“分隔符”)
"""

list_result = "a-b-c-d".split("-")
print(list_result)

# 应用:
# 将一个字符串(记录了多个数据),拆分为多个数据(一个列表)
line = "孙悟空,唐僧,猪八戒"
datas = line.split(",")
print(datas)
