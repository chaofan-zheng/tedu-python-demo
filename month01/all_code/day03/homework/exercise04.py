"""
    画出内存图
"""
data01 = 100
data02 = 200
data03 = data01 + data02 # 产生了新数据300
data01 = 200
print(data03)  # 300
