class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 编号(对学生信息的唯一标记)
        self.sid = sid

    def __str__(self):  # 对象 -> 字符串
        return "我是%s,学号是%d,今年%d岁了,考试%d分" % (self.name, self.sid, self.age, self.score)

    # 指定比较相同的依据
    def __eq__(self, other):
        return self.sid == other.sid