"""
    练习4：定义函数，将列表中大于某个值的元素设置为None
                 参数                           结果
       [34, 545, 56, 7, 78, 8]  -10->  [None,None,None,7,None,8]
       [34, 545, 56, 7, 78, 8]  -100->  [34, None, 56, 7, 78, 8]
"""
# 传入可变,修改可变 ---> 不用return
def set_None_gt_number(list_target,number):
    for i in range(len(list_target)):
        if list_target[i]  > number:
            list_target[i] = None

list01 = [34, 545, 56, 7, 78, 8]
set_None_gt_number(list01,10)
print(list01)

list02 = [34, 545, 56, 7, 78, 8]
set_None_gt_number(list02,100)
print(list02)
