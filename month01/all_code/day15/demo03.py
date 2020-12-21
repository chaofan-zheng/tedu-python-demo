"""
    Python程序结构
        根目录
            包(文件夹)
                模块(文件)
                    类
                        函数(方法)
                            语句(代码)
    导入方式同模块
        注意:路径从根目录(标记蓝色的文件夹)开始写
"""
# 我过去
import package01.package02.module02 as m

m.func01()

# 你过来
from package01.package02.module02 import func01

func01()