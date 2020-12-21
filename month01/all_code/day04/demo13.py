"""
    切片:定位多个元素
        for number in range(开始,结束,间隔)
"""
message = "我是花果山水帘洞美猴王孙悟空"
# 写法1:容器名[开始: 结束: 间隔]
# 注意:不包含结束
print(message[2: 5: 1])

# 写法2:容器名[开始: 结束]
# 注意:间隔默认为1
print(message[2: 5])

# 写法3:容器名[:结束]
# 注意:开始默认为头
print(message[:5])

# 写法4:容器名[:]
# 注意:结束默认为尾
print(message[:])

message = "我是花果山水帘洞美猴王孙悟空"
# 水帘洞
print(message[5:8])
# 花果山水帘洞美猴王
print(message[2: -3])
# 空
print(message[1: 1])
#　是花果山水帘洞美猴王孙悟空
print(message[1: 100])
# 孙悟空
print(message[-3:])
print(message[:5])
# 特殊：空悟孙王猴美洞帘水山果花是我
print(message[::-1])
# 空孙猴洞水果是
print(message[::-2])

