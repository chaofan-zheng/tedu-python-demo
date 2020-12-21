# 练习：
# 生成10--30之间能被3或者5整除的数字
# [10, 12, 15, 18, 20, 21, 24, 25, 27]

# list_result = []
# for number in range(10,31):
#     if number % 3 ==0 or number % 5 ==0:
#         list_result.append(number)
# print(list_result)
list_result = [number for number in range(10, 31) if number % 3 == 0 or number % 5 == 0]
# 生成5 -- 20之间的数字平方
# [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
list_result = [number ** 2 for number in range(5, 21)]
print(list_result)
