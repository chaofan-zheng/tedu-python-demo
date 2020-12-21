"""
    模块导入
"""
# "我过去"
# 原理:创建变量,关联目标模块
# 语法:import 模块名
# 使用:模块名.成员
# import module01
#
# module01.func01()
# module01.func02()

# "你过来"
# 原理:将目标模块的成员导入到当前模块作用域中
# 语法:from 模块名 import 成员
# 使用:成员
# 注意:命名冲突

# from module01 import func01,func02
from module01 import *


def func01():
    print("demo01 -- func01")


func01()
func02()
