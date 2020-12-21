"""
    练习1：遍历商品控制器
        目标:商品控制器对象,能够参与for循环.
        推导过程:
            1. 因为for首先调用可迭代对象的__iter__函数
               所以商品控制器类添加__iter__函数
            2. 因为for第二步调用迭代器的__next__函数
                所以商品控制器的__iter__函数返回商品迭代器对象CommodityIterator
            3. 因为商品迭代器的__next__函数需要返回商品控制器列表元素
                所以商品迭代器创建构造函数接收列表
            4. 因为for循环会重复调用__next__函数,返回下一个元素
                所以商品迭代器在__next__函数中先增加所以再返回数据
"""


class CommodityController:
    def __init__(self):
        self.__list_commodity = []

    def add_commodity(self, commodity):
        self.__list_commodity.append(commodity)

    def __iter__(self):
        return CommodityIterator(self.__list_commodity)

class CommodityIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]

controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)
