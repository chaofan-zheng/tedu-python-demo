"""
    元组应用
"""
month = int(input("请输入月份:"))
year = int(input("请输入年份:"))
# if 1 <= month <= 12:
#     if month == 2:
#         print("29天")
#     # elif month == 4 or month == 6 or month == 9 or month == 11:
#     elif month in (4, 6, 9, 11):
#         print("30天")
#     else:
#         print("31天")
# else:
#     print("月份有误")

day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
days_of_month = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(days_of_month[month - 1])
