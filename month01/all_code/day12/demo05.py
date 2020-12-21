"""
    内置可重写函数
        复合运算符重载

"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴分量是{self.x},y轴分量是{self.y}"

    # +
    def __add__(self, other):
        if type(other) == Vector2:
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector2(x, y) # 返回新对象

    # +=
    def __iadd__(self, other):
        if type(other) == Vector2:
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self # 返回现有对象


pos01 = Vector2(3, 1)
print(id(pos01))
pos01 += Vector2(2, 3) # 自动调用iadd
print(id(pos01))
print(pos01)

data01 = [10, 20]
print(id(data01))
# 如果是可变对象,+=会在原对象基础上修改
# 如果是不可变对象,+=会创建新对象
data01 = data01 + [30, 40]
print(id(data01))
print(data01)  # [10, 20, 30, 40]
