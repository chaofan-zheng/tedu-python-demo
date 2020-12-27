"""
练习1： 编写一个程序，删除主目录下 “下载”
文件夹中大小 小于1kb的文件
"""
import os

dir = "/home/tarena/下载/"

for file in os.listdir(dir):
    filename = dir + file
    # 普通文件 and 小于1kb
    if os.path.getsize(filename) < 1024 and \
            os.path.isfile(filename):
        os.remove(filename) # 删除文件
