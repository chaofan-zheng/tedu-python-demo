"""
文件打开操作
"""
# 打开文件
# file = open("3.txt",'r') # 默认r
# file = open("file.txt",'w') # 写 文件不存在创建，存在清空

# 追加　，文件内容不清空
file = open("file.txt",'a')
print(file)

# 读写操作

# 关闭文件
file.close()