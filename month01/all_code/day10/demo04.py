"""
    类变量:对象相同数据
        创建:在类中方法外
            变量名 = 数据

        使用:
            类名.变量名

    类方法

"""


class ICBC:
    # 类变量:对象相同数据(总行信息)
    total_money = 1000000

    # 类方法:操作类变量
    @classmethod
    def print_total_money(cls):
        # 建议:在类方法中通过cls代替类名操作类变量
        # print("总行的钱,还剩下%d元" % ICBC.total_money)
        print("总行的钱,还剩下%d元" % cls.total_money)

    def __init__(self, name="", money=0):
        # 实例变量:对象不同数据(支行信息)
        self.name = name
        self.money = money
        # 总行的钱减少
        ICBC.total_money -= money


tian_tan = ICBC("天坛支行", 100000)
xi_dan = ICBC("西单支行", 200000)
# print(ICBC.total_money)
ICBC.print_total_money()  # print_total_money(ICBC)
