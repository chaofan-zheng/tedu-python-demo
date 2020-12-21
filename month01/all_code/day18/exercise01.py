"""
练习：
    1. 在商品列表，获取所有名称与单价
    2. 在商品列表中，获取所有单价小于10000的商品
    3. 对商品列表，根据单价进行降序排列
    4. ([1,1],[2,2,2],[3,3,3])
       获取元组中长度最大的列表
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

for item in map(lambda item: (item.name, item.price), list_commodity_infos):
    print(item)

# for item in filter(lambda item:item.price < 10000,list_commodity_infos):
#     print(item.__dict__)

# 生成器 --> 容器
datas = tuple(filter(lambda item: item.price < 10000, list_commodity_infos))
print(datas[0].__dict__)
print(datas[-1].__dict__)

new_data = sorted(list_commodity_infos, key=lambda item: item.price, reverse=True)
# sorted 返回排好序的新列表,没有改变原列表
# 如果需要修改原列表, 需要下一行代码
list_commodity_infos[:] = new_data
print(new_data)

tuple01 = ([1, 1], [2, 2, 2], [3, 3, 3])
print(max(tuple01, key=lambda item: len(item)))
