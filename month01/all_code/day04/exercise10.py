# 在终端中获取一个整数，作为边长，打印矩形。
number = int(input("请输入整数："))
for count in range(number):  # 0 1 2 3 4
    # 开头和结尾
    if count == 0 or count == number - 1:
        print("*" * number)
    else:  # 中间
        print("*%s*" % (" " * (number - 2)))
