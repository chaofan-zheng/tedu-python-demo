"""
    练习2：
        根据月日,计算是这一年的第几天.
        公式：前几个月总天数 + 当月天数
    例如：5月10日
        计算：31  29  31  30 + 10
"""
year = int(input("请输入年份:"))
month = int(input("请输入月份:"))  # 5
day = int(input("请输入日:"))
# 构建容器(每月天数)
day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
days_of_month = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# total_days = 0
# for i in range(month - 1):
#     total_days += days_of_month[i]
# days_of_month[0]
# days_of_month[1]
# days_of_month[2]
# days_of_month[3]
# day
total_days = sum(days_of_month[:month - 1])
total_days += day
print(total_days)

