"""
    练习：使用闭包模拟以下情景：
        在银行开户存入10000
        购买xx商品花了xx元
        购买xx商品花了xx元
"""


def create_bank_account(money):
    def buy(commodity, price):
        nonlocal money
        money -= price
        print("购买%s商品花了%d元还剩下%d元" % (commodity, price, money))

    return buy


# 外部函数调用一次
action = create_bank_account(10000)
# 内部函数调用多次
action("飞机", 500)
action("大炮", 800)
action("坦克", 1000)
