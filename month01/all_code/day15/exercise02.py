"""
    练习2：定义函数,根据生日(年月日),计算活了多天.
    输入：2010   1   1
    输出：从2010年1月1日到现在总共活了3910天
"""
import time


def get_life_days(year, month, day):
    time_tuple = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
    # 当前时间 - 出生时间
    life_second = time.time() - time.mktime(time_tuple)
    return life_second / 60 / 60 / 24


print(get_life_days(1995, 2, 26))
