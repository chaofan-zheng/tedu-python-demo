"""
    只读属性:
    创建桌子类
        数据：品牌,材质,尺寸(长,宽,高)
"""


class Desk:
    def __init__(self):
        self.__brand = "乐歌"
        self.__material = "复合板材"
        self.__size = (112, 29.5, 16)

    @property
    def brand(self):
        return self.__brand

    @property
    def material(self):
        return self.__material

    @property
    def size(self):
        return self.__size


lege = Desk()
print(lege.brand)
print(lege.material)
print(lege.size)
