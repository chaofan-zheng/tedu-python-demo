"""
    字符串字面值
"""
# 1. 各种写法
# 双引号
name01 = "悟空"
# 单引号
name02 = '悟空'
# 三引号: 可见即所得
name03 = '''
孙
    悟
空'''
print(name03)
name03 = """悟空"""

# 2. 引号冲突
message = '我是"孙悟空"同学.'
message = "我是'孙悟空'同学."
message = """我是'孙'悟"空"同学."""

# 3. 转义字符:能够改变含义的特殊字符
# \"   \'   \\   换行\n
message = "我是\"孙悟空\"同\n学."
print(message)
url = "C:\\antel\\bxtremeGraphics\\cUI\\desource"
# 原始字符
url = r"C:\antel\bxtremeGraphics\cUI\desource"
print(url)