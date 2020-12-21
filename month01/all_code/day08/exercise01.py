"""
    练习1：创建计算治愈比例的函数
    confirmed = int(input("请输入确诊人数:"))
    cure = int(input("请输入治愈人数:"))
    cure_rate = cure / confirmed * 100
    print("治愈比例为" + str(cure_rate) + "%")
"""


# 形式参数
def calculate_cure_ratio(confirmed, cure):
    """
        计算治愈比例
    :param confirmed:确认人数
    :param cure:治愈人数
    :return:治愈比例
    """
    cure_rate = cure / confirmed * 100
    return cure_rate


# rate = calculate_cure_ratio(500,480)
# print(rate)
print(calculate_cure_ratio(500, 480))
