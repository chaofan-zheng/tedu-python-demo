"""
    根据工资计算个人社保缴纳费用
    步骤：在终端中录入工资,根据公式计算,显示缴纳费用
    公式：养老保险8% + 医疗保险2% + 3元 + 失业保险0.2% + 公积金12%
"""
salary_before_tax = float(input("请输入税前工资："))
social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
print("个人需要缴纳社保费用：" + str(social_insurance))
