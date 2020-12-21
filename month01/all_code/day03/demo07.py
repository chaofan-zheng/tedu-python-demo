"""
    if else if 语句
        if 条件1:
            满足条件1执行的代码
        elif 条件2:
            不满足条件1,但满足条件2执行的代码
        else:
            以上条件都不满足执行的代码

        if 条件1:
            满足条件1执行的代码

        if 条件2:
            满足条件2执行的代码
        else:
            不满足条件2执行的代码

        调试:
            定义:
                让程序中断,逐语句执行代码,
                审查程序执行过程与变量取值(variables面板)
            步骤:
                1. 加断点(在可能出错的物理行)
                2. 开始调试
                3. 逐语句执行(待命中断点后按F8)
                4. 关闭程序
"""
number = int(input("请输入数字:"))
if number > 0:
    print("正数")
elif number < 0:
    print("负数")
else:
    print("零")

# if number > 0:
#     print("正数")
# if number < 0:
#     print("负数")
# if number == 0:
#     print("零")
