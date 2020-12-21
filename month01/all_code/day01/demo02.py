"""
    汇率转换器
"""
# 1. 获取数据 - 美元
usd = float(input("请输入美元："))

# 2. 逻辑处理 - 美元 * 6.6977
cny = usd * 6.6977

# 3. 显示结果 - xxx美元=xxx人民币
print(str(usd) + "美元 = " + str(cny) + "人民币")
print(cny)
