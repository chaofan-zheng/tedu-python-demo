"""
文件写方法 示例
"""
# 打开一个文件
file = open("file.txt",'w')

# 追加方式打开
# file = open("file.txt",'a')

# 写入内容
# file.write("hello,死鬼\n")
# n = file.write("哎呀，干啥\n")
# print("写入 %d 字节"%n)

# 将列表写入文件
data = [
    "先帝创业未半\n",
    "而中道崩殂\n"
]

file.writelines(data)

# 关闭
file.close()