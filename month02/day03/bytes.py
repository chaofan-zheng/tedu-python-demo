"""
字节串使用示例

* 所有字符串都能转换为字节串
* 并不是所有字节串都能转为字符串
"""

# 定义一个ascii字节串变量
b = b"hello world"
print(type(b))

# 定义一个非ascii字节串变量
b1 = "你好".encode()
print(b1)

# 将字节串转换为字符串
s1 = b'\xe4\xb1\xd1\xe6\xa5\xbd'.decode()
print(s1)
