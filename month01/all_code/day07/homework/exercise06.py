"""
    将列表中所有元素转换为一个字符串
    列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
    结果:我爱你python666
"""
list_message = ["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]

# "".join(list_message) # 666 是整数，不能拼接为str

str_message = "".join([str(item) for item in list_message])
print("转化后的字符串为:" + str_message)
