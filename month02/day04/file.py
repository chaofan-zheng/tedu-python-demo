"""
文件处理函数
"""
import os

print("文件大小:",os.path.getsize("my.log"))
print("文件列表:",os.listdir("."))
print("是否存在:",os.path.exists("my.lg"))
print("是否普通文件:",os.path.isfile('.'))
os.remove("my.log")