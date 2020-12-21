"""
    变量交换
"""
# 方法一：借助第三个变量
# bridegroom_name = "武大郎"
# bride_name = "潘金莲"
# temp = bridegroom_name
# bridegroom_name = bride_name
# bride_name = temp
# print("交换后的新郎：" + bridegroom_name)  #
# print("交换后的新娘：" + bride_name)  #

# 方法二：直接交换　
# a , b = b , a
bridegroom_name = "武大郎"
bride_name = "潘金莲"
bridegroom_name, bride_name = bride_name, bridegroom_name
print("交换后的新郎：" + bridegroom_name)  #
print("交换后的新娘：" + bride_name)  #
