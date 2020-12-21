"""
    跳转语句
"""
# 需求:累加1 -- 100整数
# 条件:能被3整除

# 思想:满足条件则累加
# sum_value = 0
# for number in range(1, 101):
#     if number % 3 == 0:
#         sum_value += number
# print(sum_value)

# 思想:不满足条件则跳过,否则累加
sum_value = 0
for number in range(1, 101):
    if number % 3 != 0:
        continue  # 跳过本次循环,继续下次循环
        # break # 跳出循环
    sum_value += number
print(sum_value)

