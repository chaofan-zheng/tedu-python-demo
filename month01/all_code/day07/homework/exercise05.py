"""
     4. 列表推导式练习：
         计算1970年到2050年之间所有闰年
"""
# list_year = []
# for item in range(1970, 2051):
#     if item % 4 == 0 and item % 100 != 0 or item % 400 == 0:
#         list_year.append(item)

list_year = [item for item in range(1970, 2051)
             if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]
print(list_year)
