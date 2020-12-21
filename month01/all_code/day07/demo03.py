"""
    列表推导式嵌套
"""
list_fruits = ["香蕉", "苹果", "哈密瓜"]
list_drinks = ["牛奶", "咖啡", "雪碧", "可乐"]
# list_result = []
# for fruit in list_fruits:
#     for drink in list_drinks:
#         list_result.append((fruit, drink))
# print(list_result)
list_result = [(fruit, drink) for fruit in list_fruits for drink in list_drinks]
