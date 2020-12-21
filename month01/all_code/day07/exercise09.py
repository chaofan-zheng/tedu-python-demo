# 练习2：创建函数,在终端中打印矩形.

def print_rectangle(number):
    for row in range(number):
        if row == 0 or row == number - 1:
            print("*" * number)
        else:
            print("*%s*" % (" " * (number - 2)))

print_rectangle(8)