"""
    闭包 - 应用
        逻辑连续
            从得到1000元压岁钱,到反复购买商品的过程,
            不中断,可以连续执行.
"""


def give_gife_money(money):
    print("获取%d元压岁钱" % money)

    def child_buy(commodity, price):
        nonlocal money
        money -= price
        print("购买%s花了%d元,还剩下%d元" % (commodity, price, money))

    return child_buy

action = give_gife_money(1000)
action("游戏机", 300)
action("卡带", 100)
action("手柄", 200)

# 练习：使用闭包模拟以下情景：
#     在银行开户存入10000
#     购买xx商品花了xx元
#     购买xx商品花了xx元
