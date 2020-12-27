"""
re 模块使用 2
"""
import re

s = " Alex:1996,Sunny:1998"

# 匹配第一个符合规则的字符串
result = re.search(r"(\w+):(?P<year>\d+)",s)
# 通过组序号或者名获取值
print(result.group("year"))
print(result.groupdict())

# 匹配开头位置符合规则的字符串
# result = re.match("\w+",s)
# print(result.group())


# result = re.finditer(r"\w+",s)
# # 迭代取值每次得到一个match对象
# for res in result:
#     print("匹配内容：",res.group())
#     print("所在位置:",res.span())
