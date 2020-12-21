"""
练习：
    直接打印商品对象: xx的编号是xx,单价是xx
    直接打印敌人对象: xx的攻击力是xx,血量是xx
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    # 对象 --> 字符串
    def __str__(self):
        return f"{self.cid}的编号是{self.name},单价是{self.price}"

class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return "%s的攻击力是%d,血量是%d" % (self.name, self.atk, self.hp)


jgb = Commodity(1001, "金箍棒", 32)
print(jgb)

mb = Enemy("灭霸", 1000, 5000)
print(mb)
