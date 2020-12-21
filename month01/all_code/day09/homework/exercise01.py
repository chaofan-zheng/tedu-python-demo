"""
    参照下列代码,定义函数,计算社保缴纳费用.
    salary_before_tax = float(input("请输入税前工资："))
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    print("个人需要缴纳社保费用：" + str(social_insurance))
"""


def get_social_insurance(base_pay):
    """
        获取社保缴纳费用
    """
    return 3 + base_pay * (0.08 + 0.002 + 0.02 + 0.12)



# 测试
print(get_social_insurance(5000))
get_social_insurance(8000)