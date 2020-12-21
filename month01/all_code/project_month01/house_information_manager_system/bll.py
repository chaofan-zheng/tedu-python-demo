"""
    业务逻辑层
"""
from common.iterator_tools import IterableHelper
from dal import HouseDao
from model import HouseModel


class HouseManagerController:
    """
        房源信息管理系统控制器：负责处理业务逻辑
    """

    def __init__(self):
        """
            创建房源信息管理系统控制器
        """
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self):
        """
            所有房源信息
        """
        return self.__list_houses

    def get_house_by_max_total_price(self):
        # 写法1：简单但不灵活
        # 重写模型的__gt__方法
        # return max(self.__list_houses)
        # 写法2： 内置高阶函数(性能高)
        # return max(self.__list_houses,key = lambda house:house.total_price)
        # 写法3： 自定义高阶函数(调试方便)
        return IterableHelper.get_max(self.__list_houses, lambda house: house.total_price)

    def get_house_by_min_area(self):
        return min(self.__list_houses, key=lambda item: item.area)

    def ascending_by_total_price(self):
        # 结果是排好序的列表(一个结果)
        return sorted(self.__list_houses, key=lambda element: element.total_price)

        # list_temp = self.__list_houses[:]
        # IterableHelper.order_by(list_temp,lambda element:element.total_price)
        # return list_temp

    def descending_by_area(self):
        return sorted(self.__list_houses, key=lambda element: element.area, reverse=True)

    def get_house_type(self):
        dict_result = {}
        for house in self.__list_houses:
            # 如果存在该房源类型，计数增加
            if house.house_type in dict_result:
                dict_result[house.house_type] += 1
            else:
                dict_result[house.house_type] = 1
        return dict_result
