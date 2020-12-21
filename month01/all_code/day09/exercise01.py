"""
    定义函数,根据小时、分钟、秒,计算总秒数
        调用：提供小时、分钟、秒
        调用：提供分钟、秒
        调用：提供小时、秒
        调用：提供分钟
"""


def get_total_second(hour=0, minute=0, second=0):
    return hour * 3600 + minute * 60 + second

# 位置实参
print(get_total_second(1, 2, 3))
# 关键字实参
print(get_total_second(minute=2, second=3))
# 位置实参 + 关键字实参
print(get_total_second(1, second=3))
print(get_total_second(minute=2))
