"""
    练习2：创建图形管理器
        1. 记录多种图形（圆形、矩形....）
        2. 提供计算总面积的方法.
        满足：
            开闭原则
        测试：
            创建图形管理器，存储多个图形对象。
            通过图形管理器，调用计算总面积方法.

    设计:
        封装(分):创建图形管理器类/圆形类/矩形类
        继承(隔):创建图形类,隔离图形管理器类与具体图形(圆形类/矩形类)的变化
        多态(做):具体图形(圆形类/矩形类)重写图形类的计算面积方法
"""


# ---------------架构师------------
class GraphicManager:
    def __init__(self):
        self.__all_graphic = []

    def add_graphic(self,graphic):
        # 传入的对象是一种图形(可以是任意子类)
        if isinstance(graphic,Graphic):
            self.__all_graphic.append(graphic)

    def get_total_area(self):
        total_area = 0
        for item in self.__all_graphic:
            # 编码时 调用一个父方法 - 图形
            # 运行时 执行多个子方法 - 矩形/圆形...
            total_area += item.calculate_area()
        return total_area


class Graphic:
    def calculate_area(self):
        pass


# ---------------程序员------------
class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        super().calculate_area()
        return 3.14 * self.r ** 2


class Rectangle(Graphic):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w


# ---------------入口------------
"""" 不隐藏all_graphic,就可能追加不合法的数据
manager = GraphicManager()
manager.all_graphic.append(Circle(8))
manager.all_graphic.append(Rectangle(2, 3))
manager.all_graphic.append("三角")
print(manager.get_total_area())
"""

manager = GraphicManager()
manager.add_graphic(Circle(8))
manager.add_graphic(Rectangle(2, 3))
manager.add_graphic("三角")
print(manager.get_total_area())