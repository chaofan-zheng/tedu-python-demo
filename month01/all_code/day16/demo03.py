"""
    名词解释
        迭代iteration : 在之前基础上进行重复的过程
        迭代器iterator: 执行迭代过程的对象
            一定具有__next__方法
        可迭代对象iterable: 能够创造迭代器的对象
            一定具有__iter__方法

    for 循环原理
"""
message = "我是齐天大圣孙悟空"
# for item in message:
#     print(item)
message = "我是齐天大圣孙悟空"
# 1. 获取迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
    # 3. 如果停止迭代(没有元素),则退出循环
    except StopIteration:
        break
