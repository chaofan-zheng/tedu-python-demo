"""

"""


class Wife(object):
    def __init__(self, name="", height=0, face_score=0):
        self.name = name
        self.height = height
        self.face_score = face_score

    # Python类型标注
    def __str__(self):
        return "%s的身高是%d,颜值是%d." % (self.name, self.height, self.face_score)

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.face_score < other.face_score


list_wife = [
    Wife("双儿", 170, 98),
    Wife("阿珂", 173, 100),
    Wife("苏荃", 160, 99),
    Wife("丽丽", 167, 90),
    Wife("芳芳", 168, 92),
    Wife("苏荃", 160, 99),
]
# 1. 打印:xx的身高是xx,颜值是xx.
sq = Wife("苏荃", 160, 99)
print(sq)

# 2. 判断阿珂是否在列表中
print(Wife("阿珂") in list_wife)

# 3. 计算苏荃在列表中存在的个数
print(list_wife.count(sq))

# 4. 查找颜值最高的老婆对象
max_by_face_score = max(list_wife)
print(max_by_face_score)

# 5. 根据颜值对老婆列表进行升序排列
list_wife.sort()
print(list_wife)
