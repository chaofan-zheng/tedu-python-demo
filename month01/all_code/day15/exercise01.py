"""
    练习1：定义函数,根据年月日,计算星期。
    输入：2020   9   15
    输出：星期二
"""
import time


def get_week_by_day(year, month, day):
    str_time = "%d-%d-%d" % (year, month, day)
    time_tuple = time.strptime(str_time, "%Y-%m-%d")
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week[time_tuple[6]]


week = get_week_by_day(2020, 11, 15)
print(week)
