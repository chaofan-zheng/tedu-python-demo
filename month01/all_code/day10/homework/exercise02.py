"""
    面向对象
        找谁?干嘛?

    现实事物  -抽象->  类 -具体-> 对象

2. 创建桌子类
        数据：品牌,材质,尺寸(长,宽,高)
   创建电脑类
        数据:型号,CPU型号,内存大小,硬盘大小
        行为：开机,关机
"""


# 现实事物  -抽象-> 类　-具体-> 对象

class Desk:
    def __init__(self, brand="", material="", size=()):
        self.brand = brand
        self.material = material
        self.size = size


class Computer:
    def __init__(self, model_number="", cpu="", memory=0, hard_disk=()):
        self.model_number = model_number
        self.cpu = cpu
        self.memory = memory
        self.hard_disk = hard_disk

    def starting_up(self):
        print(self.model_number, "开机")

    def shutdown(self):
        print(self.model_number, "关机")


lege = Desk("乐歌", "复合板材", (112, 29.5, 16))
print(lege.size)
print(lege.__dict__)

alienware = Computer("外星人ALW17M", "Intel i7", 16, (256, 1024))
# starting_up(alienware)
alienware.starting_up()
alienware.shutdown()
print(alienware.__dict__)
