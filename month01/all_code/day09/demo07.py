"""
    面向对象：软件编程思想
        找谁　干嘛?

    现实事物  -抽象->   类(模板)     -具体->   对象
       车           class Car:    Car(xx,xx,xx)
                      车牌         京E0001
                      品牌          奔驰
                      颜色          白色
"""


# 创建类(抽象化)
class Wife:
    """
        自定义类 - 老婆
    """
    # 数据
    def __init__(self, name, face_score=0, money=0):
        self.name = name
        self.face_score = face_score
        # 创建参数快捷键:atl + 回车
        self.money = money

    # 行为 - 方法(函数)
    def play(self):
        print(self.name + "在玩")


# 创建对象(具体化)
jian_ning = Wife("建宁", 93, 10000000)
print(jian_ning.money)
jian_ning.play() # play(jian_ning)
