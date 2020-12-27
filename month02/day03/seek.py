"""
文件偏移量
"""
file = open("file.txt","wb+")

file.write("2020-11-三十".encode())
file.flush()

print("文件偏移量：",file.tell())

# 设置文件偏移量
file.seek(-6,2)

# file.write(b"28")

date = file.read()
print(date.decode())

file.close()
