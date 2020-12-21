"""
练习2：二维列表
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
1. 将第一行从左到右逐行打印
	效果：1
		  2
          3
          4
          5
2. 将第二行从右到左逐行打印
	效果：10
		  9
          8
          7
          6
3. 将第三列行从上到下逐个打印
	效果：3
		  8
          13
4. 将第四列行从下到上逐个打印
	效果：14
		  9
          4
5. 将二维列表以表格状打印
	效果：1 2 3 4 5
		  6 7 8 9 10
		  11 12 13 14 15
"""
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
# 1. 将第一行从左到右逐行打印
# list01[0][0]
# list01[0][1]
# list01[0][2]
# list01[0][3]
# list01[0][4]

# len(list01) 结果是3,表示二维列表行数
# len(list01[0]) 结果是5,表示二维列表第一行的总数(列数)
for c in range(len(list01[0])):
    print(list01[0][c])

for item in list01[0]:
    print(item)

# 2. 将第二行从右到左逐行打印
#  list01[1][4]
#  list01[1][3]
#  list01[1][2]
#  list01[1][1]
#  list01[1][0]
for c in range(len(list01[1])-1, -1, -1):
    print(list01[1][c])

# 3. 将第三列行从上到下逐个打印
# list01[0][2]
# list01[1][2]
# list01[2][2]
for r in range(len(list01)):
    print(list01[r][2])

# list01[2][3]
# list01[1][3]
# list01[0][3]

# 4. 将第四列行从下到上逐个打印
for r in range(len(list01)-1,-1,-1):
    print(list01[r][3])

# 5. 将二维列表以表格状打印
# [0][0]  [0][1]   [0][2]   [0][3]  [0][4]
# [1][0]  [1][1]   [1][2]   [1][3]  [1][4]
# [2][0]  [2][1]   [2][2]   [2][3]  [2][4]
# for c in range(5):
#     print(list01[0][c],end = " ")
# print()
#
# for c in range(5):
#     print(list01[1][c],end = " ")
# print()
# for r in range(3):#      0      1      2
#     for c in range(5):# 01234
#         print(list01[r][c],end = " ")
#     print()
for r in range(len(list01)):#      0      1      2
    for c in range(len(list01[r])):# 01234
        print(list01[r][c],end = "\t")
    print()

for line in list01:
    for item in line:
        print(item,end ="\t")
    print()