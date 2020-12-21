"""
    练习：在终端中输入一个整数，如果是奇数为变量state赋值"奇数",否则赋值"偶数"。
    效果：
        请输入数字:6
    state变量存储的是：偶数
"""
# if int(input("请输入整数:")) % 2 != 0:
#     state = "奇数"
# else:
#     state = "偶数"


# if int(input("请输入整数:")) % 2:
#     state = "奇数"
# else:
#     state = "偶数"

state = "奇数" if int(input("请输入整数:")) % 2 else "偶数"
print(state)
