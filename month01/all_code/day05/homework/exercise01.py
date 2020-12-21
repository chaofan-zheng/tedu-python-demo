"""
    在终端中录入4个同学年龄,打印最小的年龄。
"""
age01 = int(input("请输入第1个同学年龄："))
age02 = int(input("请输入第2个同学年龄："))
age03 = int(input("请输入第3个同学年龄："))
age04 = int(input("请输入第4个同学年龄："))
min_age = age01
if min_age > age02:
    min_age = age02
if min_age > age03:
    min_age = age03
if min_age > age04:
    min_age = age04
print("年龄最小值是" + str(min_age))
