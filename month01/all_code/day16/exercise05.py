# 练习3：创建自定义range类，实现下列效果.
class MyRangeIterator:
    def __init__(self, end):
        self.__start = -1
        self.__end = end

    def __next__(self):
        self.__start += 1
        if self.__start > self.__end - 1:
            raise StopIteration()
        return self.__start

class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        return MyRangeIterator(self.__stop)

# 循环一次  计算一次  返回一次
# for number in MyRange(5):
#     print(number)# 0 1 2 3 4
m01 = MyRange(999999999999999999999999999999)
iterator = m01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
