"""
    标准库模块
        time时间
"""
import time

# 人类时间:公园元年 ~  ...
# 今天:2020年11月19日
# 时间元组:年/月/日/时/分/秒/星期/年的第几天/与夏令时偏移;量
print(time.localtime())

# 机器时间:1970年元旦 ~ ...
# 今天:1605776852.7242818
# 时间戳:经过的秒数
print(time.time())

# 时间戳  --> 时间元组
time_tuple = time.localtime( 1605776852.7242818  )
print(time_tuple[6]) # 获取星期
print(time_tuple[:3]) # 获取年月日

# 时间元组  --> 时间戳
print(time.mktime(time_tuple)) # 1605776852

# 时间元组 --> 字符串
print(time.strftime("%y/%m/%d %H:%M:%S",time_tuple))
print(time.strftime("%Y/%m/%d %H:%M:%S",time_tuple))

# 字符串 --> 时间元组
print(time.strptime("2020/11/19 17:07:32","%Y/%m/%d %H:%M:%S"))




