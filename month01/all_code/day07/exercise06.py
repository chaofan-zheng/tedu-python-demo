"""
    练习1:请排列出两个色子可以组成的所有可能(列表)
    练习2:请排列出三个色子可以组成的所有可能(列表)
    色子1~6  range(1,7)
    色子1~6  range(1,7)
"""
# list_result = []
# for x in range(1,7):
#     for y in range(1,7):
#         list_result.append((x,y))
# list_result = [(x, y) for x in range(1, 7) for y in range(1, 7)]

# list_result = []
# for x in range(1,7):#                 1
#     for y in range(1,7):#     1    2    3 ...  6
#         for z in range(1,7):#1~6  1~6  1~6
#             list_result.append((x,y,z))

list_result = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
print(list_result)
