"""
    真值表达式
"""
# bool 类型转换
# 转换结果为false:0  0.0  ""   None
print(bool(None))

if "abc":  # bool("abc")
    print("满足条件")
else:
    print("不满足条件")

content = input("请输入内容:")
# if content != "": # 输入的不是空字符串
if content: # 有值
    print("您输入的是:"+content)
else:
    print("您没有输入内容")