"""
    使用for-for画出下列图形
        *#*#
        *#*#
        *#*#
        *#*#
        *#*#
"""
for r in range(5):
    for c in range(4):
        if c % 2 ==0:
            print("*",end = "")
        else:
            print("#",end = "")
    print()