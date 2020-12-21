"""
    索引:定位单个元素
        容器名[整数]　
        建议:靠前元素使用正向索引定位
            靠后元素使用反向索引定位
"""
#          0 1 2 3 .....         14-1  [正向索引]
message = "我是花果山水帘洞美猴王孙悟空"
#         -14                 -2-1     [反向索引]
print(message[0])
# 水
print(message[5])
# 猴
print(message[9])
print(message[-5])
# IndexError: string index out of range
# print(message[100])