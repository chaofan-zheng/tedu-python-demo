"""
    画出下列代码内存图
"""
map = [
    [2, 2, 8, 16],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]
list_merge = map[0]
list_merge[0] = 0 # 通过list_merge修改数据,等同于通过map修改
print(map[0][0])# 0

list_merge = map[1][::-1]# 创建新容器[2,0,2,4]
list_merge[0] = 0# [0,0,2,4]     修改list_merge第一个元素
map[1][::-1] = list_merge
print(map[1])# [ 4,2,0,0]　　　　 相当于修改map最后一个元素
