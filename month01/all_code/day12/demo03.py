"""
    内置可重写函数
        运算符重载
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴分量是{self.x},y轴分量是{self.y}"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x,y)

pos01 = Vector2(3,1)
pos02 = Vector2(2,5)
pos03 = pos01 + pos02# pos01.__add__(pos02)
print(pos03)

