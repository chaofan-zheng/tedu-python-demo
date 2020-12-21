"""
    在终端中录入3个疫情省份的确诊人数
    最后打印最大值、最小值、平均值.（使用内置函数实现）
"""
list_confirmed_num = []
for i in range(3):  # 0  1  2
    # confirmed_num = int(input("请输入第%d个确诊人数：" % (i + 1)))
    confirmed_num = int(input(f"请输入第{i + 1}个确诊人数："))
    list_confirmed_num.append(confirmed_num)

print(max(list_confirmed_num))
print(min(list_confirmed_num))
print(sum(list_confirmed_num) / len(list_confirmed_num))
