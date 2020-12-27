"""
re 模块使用
"""
import re

s = "Alex:1996,Sunny:1998"
pattern = r"(\w+):(\d+)"

# 使用## 替换正则表达式匹配到的内容
result = re.sub(r"\W+","##",s)
print(result)

# 根据正则匹配到的内容分割字符串
result = re.split("\W+",s,2)
print(result)

# 如果正则表达式中有组，那么只能得到组所对应内容
result = re.findall(pattern,s)
print(result)




