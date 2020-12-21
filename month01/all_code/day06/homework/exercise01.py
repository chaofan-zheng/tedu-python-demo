"""
    1. 根据列表中的数字,重复生成*.
        list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    效果：
        *
        **
        ***
        ****
        *****
        ****
        ***
        **
        *
"""
list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# 依次 全部  读取
for number in list01:
    print("*" * number)

# for i in range(len(list01)):
#     print("*" * list01[i])
