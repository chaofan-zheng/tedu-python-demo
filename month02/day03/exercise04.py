"""
重点代码 ！！

练习4： 假设在当前文件夹下有一个图片timg.jfif
请编写一个函数，将该文件名传入，通过执行函数将其
复制一份到 主目录下
注意： 考虑可能文件比较大，不允许一次性读取

逻辑提示： 边从原来的文件读取内容，再将内容写入新文件
"""


def copy(filename):
    """
    :param filename: 要拷贝的文件
    """
    fr = open(filename, 'rb')  # 原文件
    fw = open("/home/tarena/" + filename, 'wb')
    # 边读边写
    while True:
        data = fr.read(1024)
        # 如果读取到空，则表示文件拷贝结束
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

copy("timg.jfif")