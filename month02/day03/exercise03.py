"""
练习3：
请在屏幕上使用input函数输入一首古诗
《悯农》
将其写入到文件file.txt中
要求每次input只输入一句

锄禾日当午，
汗滴禾下土。
谁知盘中餐，
粒粒皆辛苦。
"""

# 打开文件  w
file = open("file.txt", 'w')

# 循环的输入写入文件
while True:
    data = input(">>")
    if not data:
        break
    file.write(data + '\n')

file.close()
