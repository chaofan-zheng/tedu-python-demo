"""
    练习4：以面向对象思想,描述下列情景.
    玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).
"""


class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self, enemy):
        print("攻击")
        enemy.damage(self.atk)

class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("受伤啦,血量还剩", self.hp)

player = Player(50)
enemy = Enemy(100)
player.attack(enemy)
