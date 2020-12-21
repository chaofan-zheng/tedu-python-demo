"""
    项目根目录:主模块所在文件夹
    主模块:第一次运行的文件
    导入模块是否成功的唯一标准:
        导入路径 + 系统路径 = 真实路径
    查看系统路径:
        import sys
        print(sys.path) # 系统路径
"""
import sys

print(sys.path)  # 系统路径