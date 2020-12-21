"""
    读写属性:
    创建技能类，并保护数据在有效范围内
        数据：技能名称,冷却时间,  攻击力度,  消耗法力
                 0 -- 120  0 -- 200    0 -- 100


"""


class Skill:
    def __init__(self, name="", cd=0, atk=0, cost_sp=0):
        self.name = name
        self.cd = cd
        self.atk = atk
        self.cost_sp = cost_sp

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        if 0 <= value <= 120:
            self.__cd = value
        else:
            raise Exception("冷却时间超过范围")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 200:
            self.__atk = value
        else:
            raise Exception("攻击力超过范围")

    @property
    def cost_sp(self):
        return self.__cost_sp

    @cost_sp.setter
    def cost_sp(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        self.__cost_sp = value


xlsbz = Skill("降龙十八掌", 60, 200, 80)
print(xlsbz.name)
print(xlsbz.atk)
print(xlsbz.cost_sp)
print(xlsbz.cd)
