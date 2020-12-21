"""
    可迭代对象工具集
"""


class IterableHelper:
    """
        可迭代对象助手
    """

    # 静态方法:常用的工具,独立性强,不依赖于实例成员和类成员
    @staticmethod
    def find_all(iterable, func):
        """
            在可迭代对象中,根据条件查找多个元素
        :param iterable: 可迭代对象
        :param func: 函数类型的条件
        :return: 生成器
        """
        for item in iterable:
            if func(item):
                yield item

    @staticmethod
    def find_single(iterable, func):
        """
            在可迭代对象中,根据条件查找单个元素
        :param iterable: 可迭代对象
        :param func: 函数类型的条件
        :return: 满足条件的对象
        """
        for item in iterable:
            if func(item):
                return item

    @staticmethod
    def select(iterable, func):
        """

        :param iterable:
        :param func:
        :return:
        """
        for item in iterable:
            yield func(item)

    @staticmethod
    def get_max(iterable, func):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(max_value) < func(iterable[i]):
                max_value = iterable[i]
        return max_value
