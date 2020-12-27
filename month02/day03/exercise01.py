"""
练习1：
一次读取5个字符，将file.txt
文件从头到尾读取打印出来，打印
内容与原文件保持一直
"""

# 函数
def print_file(filename):
    # 默认读
    file = open(filename)
    while True:
        data = file.read(1024)
        # 读到结尾会data为空
        if not data:
            break
        # 每次打印不换行
        print(data,end="")
    file.close()

print_file("file.txt")