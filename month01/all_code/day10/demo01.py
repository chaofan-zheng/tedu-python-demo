"""
    实例成员
        实例变量:s个体的数据
        实例方法:个体的行为(操作实例变量)
"""
# name = "双二" # 全局变量内存中只有一份
class Wife:
    def __init__(self, name=""):
        self.name = name  # 每个对象都有一份

    def play(self):
        print(self.name + "在玩耍")

jian_ning = Wife("建宁")  # 在内存中分配空间,存储name
shuagn_er = Wife("双儿")  # 在内存中分配空间,存储name
print(jian_ning.name)

# Python内置实例变量,存储的是对象所有实例变量
#  {'name': '建宁'}
print(jian_ning.__dict__)
