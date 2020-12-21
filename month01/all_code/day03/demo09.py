"""
    条件表达式
        结果 = 满足条件的结果 if 条件 else 不满足条件的结果
        根据条件给变量进行赋值
"""
# if input("请输入性别:") == "男":
#     value = 1
# else:
#     value = 0

value = 1 if input("请输入性别:") == "男" else 0

print("性别编号是:" + str(value))
