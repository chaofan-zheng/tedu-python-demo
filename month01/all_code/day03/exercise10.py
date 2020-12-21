"""
    练习1：
    让下列代码重复执行，输入y继续(不输入y则退出)
"""
while True:
    sex = input("请输入性别:")
    if sex == "男":
        print("您好先生")
    elif sex == "女":
        print("您好女士")
    else:
        print("未知")

    if input("输入y继续:") != "y":
        break
