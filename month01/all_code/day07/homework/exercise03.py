"""
    3. 将列表中整数的十位不是3和7和8的数字存入另外一个列表
        list03 = [135, 63, 227, 675, 470, 733, 3127]
    结果:[63, 227, 3127]
"""
list03 = [135, 63, 227, 675, 470, 733, 3127]
result = []
for item in list03:
    # 将数字转换为字符串,再通过索引取出某一位
    unit = str(item)[-2]
    if unit in ("3", "7", "8"):
        continue
    result.append(item)
print(result)
