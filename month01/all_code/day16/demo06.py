# MyRange2.0

class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        start = 0
        while start < self.__stop:
            yield start
            start +=1

for number in MyRange(5):
    print(number)# 0 1 2 3 4

# MyRange3.0
# 生成器函数
"""
class generator: # 生成器 = 可迭代对象 + 迭代器
    def __iter__(self):
        return self
    
    def __next__(self):
        .... 
"""
def my_range(stop):
    start = 0
    while start < stop:
        yield start
        start +=1
# for number in my_range(5):
#     print(number)# 0 1 2 3 4
m01 = my_range(5)
print(m01) 

iterator =m01 .__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
    # 3. 如果停止迭代(没有元素),则退出循环
    except StopIteration:
        break