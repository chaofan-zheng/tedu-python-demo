"""
    如果需要调用自定义类型容器的相关函数,
    必须在自定义类型中重写相应函数
    例如: == 或者 count -->  __eq__
         min 或者 sort --> __lt__
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴分量是{self.x},y轴分量是{self.y}"

    # 确定两个对象是否相同的判断依据
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 确定两个对象大小的比较依据
    def __lt__(self, other):
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2


# 以下功能必须重写__eq__
v01 = Vector2(1, 2)
v02 = Vector2(1, 2)
print(v01 == v02)  # 默认按照地址比较

list_vector = [
    Vector2(1, 1),
    Vector2(3, 3),
    Vector2(2, 2),
    Vector2(5, 5),
    Vector2(4, 4),
]
print(Vector2(3, 3) in list_vector)
print(list_vector.count(Vector2(5, 5)))

# 以下功能必须重写__lt__
print(min(list_vector))
list_vector.sort()
for item in list_vector:
    print(item)
