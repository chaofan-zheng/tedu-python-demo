"""
读写缓冲区
"""
# 行缓冲打开
# file = open("file.txt",'w',buffering=1)

# 设置缓冲大小
file = open("file.txt",'wb',buffering=10)

while True:
    msg = input(">>")
    if not msg:
        break
    file.write(msg.encode())
    # file.flush() # 刷新缓冲

file.close()