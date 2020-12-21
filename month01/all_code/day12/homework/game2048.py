"""
    2048核心算法
"""
list_merge = [2, 0, 0, 2]

# 1. 定义函数　zero_to_end()
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

# zero_to_end()
# print(list_merge)


# 2. 定义函数　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
def merge():
    """
        合并数据
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    # len() - 1 : 因为最后一个元素不用与下一个比较
    #             所以-1去掉最后一个元素
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)

# merge()
# print(list_merge)

# 作业
map = [
    [2,0,0,2],
    [2,0,2,0],
    [2,4,2,0],
    [4,4,4,2],
]
# 定义函数,实现向左移动(操作map)
# 思想:取出每行交给list_merge,再调用merge函数处理数据

# 定义函数,实现向右移动(操作map)
# 思想:取出每行反向切片交给list_merge,
#     再调用merge函数处理数据(操作新列表)
#     最后还给map
 