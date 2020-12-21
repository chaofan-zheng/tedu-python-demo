# 练习1：创建列表,使用迭代思想,打印每个元素.
list01 = [4, 4, 5, 65, 7, 8]
iterator = list01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

# 练习2：创建字典,使用迭代思想,打印每个键值对.
dict01 = {"a": 1, "b": 2, "c": 3}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
