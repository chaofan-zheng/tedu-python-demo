"""
    练习：在终端中输入一个年份，如果是闰年为变量day赋值29,否则赋值28。
          闰年条件：年份能被4整除但是不能被100整除
                    年份能被400整除
"""
year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day = 29
else:
    day = 28

# 不建议使用下列代码
# year = int(input("请输入年份:"))
# if not year % 4  and year % 100 or not year % 400 :
#     day = 29
# else:
#     day = 28



