"""
    实例变量应用
"""

# 练习:将面向过程代码day10/homework/exercise01
#     修改为面向对象代码
# --------------------------类--------------------------
class Commodity:
    def __init__(self,cid,name,price):
        self.cid = cid
        self.name = name
        self.price = price

list_commodity_infos = [
    Commodity(1001,"屠龙刀",10000),
    Commodity(1002,"倚天剑",10000),
    Commodity(1003,"金箍棒",52100),
    Commodity(1004,"口罩",20),
    Commodity(1005,"酒精",30),
]


# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


def print_single_commodity(commodity):
    print(f"编号:{commodity.cid},商品名称:{commodity.name},商品单价:{commodity.price}")

# 1.  定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_infos():
    for commodity in list_commodity_infos:
        print_single_commodity(commodity)

# 2.  定义函数,打印商品单价小于2万的商品信息
def print_price_in_2w():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_single_commodity(commodity)

