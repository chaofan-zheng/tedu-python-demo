"""
with 打开文件
"""
with open("file.txt") as file:
    # 语句块内部可以使用file
    data = file.read()
    print(data)

# 语句块结束file会自动消失，不需close