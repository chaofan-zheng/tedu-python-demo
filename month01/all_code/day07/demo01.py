"""
    for - for
        外层循环执行1次  (控制行)
        内层      多   (控制列)
"""
"""
print("老王", end=" ")
print("老王", end=" ")
print("老王", end=" ")
print("老王", end=" ")
print("老王", end=" ")
print() # 换行
print("老王", end=" ")
print("老王", end=" ")
print("老王", end=" ")
print("老王", end=" ")
print("老王", end=" ")
print() # 换行
"""
# for c in range(5):# 0 1 2 3 4
#     print("老王", end=" ")
# print() # 换行
#
# for c in range(5):# 0 1 2 3 4
#     print("老王", end=" ")
# print() # 换行

for r in range(6):  # 0           1
    for c in range(3):  # 0 1 2 3 4   0 1 2 3 4
        print("老王", end=" ")
    print()  # 换行

for r in range(5):
    for c in range(6):
        if r % 2 == 0:
            print("#", end="")
        else:
            print("*", end="")
    print()
