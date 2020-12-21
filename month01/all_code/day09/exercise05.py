"""
    练习：创建手机类
        数据：品牌、价格、颜色
        行为：通话
        实例化两个对象并调用其函数
"""


# 类命名规范:所有单词首字母大写,不要下划线隔开
class MobilePhone:
    def __init__(self, brand, price=5000, color="白色"):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand + "通话")


huawei = MobilePhone("华为", 7000, "黑色")
iphone = MobilePhone("苹果", 6000)

huawei.call()  # call(huawei)
iphone.call()  # call(iphone)
