"""
读取文件内容 示例
"""

# 打开文件
file = open("file.txt","r")

# 二进制打开
# file = open("file.txt","rb")

# 读取文件内容
# data = file.read(5)
# print(data)
# data = file.read()
# print(data)

# 按行读取
# data = file.readline()
# print(data)
# data = file.readline(3)
# print(data)

# 将文件内容读取为一个列表
# lines = file.readlines()
# print(lines)

# 迭代获取
for line in file:
    print(line)

# 关闭文件
file.close()


