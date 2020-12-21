"""
    延长软件生命
    while True:
        循环体
        if 条件:
            break
"""
# 死循环
while True:
    if input("请输入职位:") == "高管":
        print("娶你")
    else:
        print("继续努力")
    if input("请输入q键退出:") == "q":
        break  # 跳出循环
