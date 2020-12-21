# 练习1：定义函数,在列表中找出所有偶数
# [43,43,54,56,76,87,98]

list01 = [43, 43, 54, 56, 76, 87, 98]


def get_evens():
    for item in list01:
        if item % 2 == 0:
            yield item


for item in get_evens():
    print(item)

# 练习2. 定义函数,在列表中找出所有数字
#  [43,"悟空",True,56,"八戒",87.5,98]
list02 = [43, "悟空", True, 56, "八戒", 87.5, 98]


def get_numbers():
    for item in list02:
        if type(item) in (int, float):
            yield item

for item in get_numbers():
    print(item)
