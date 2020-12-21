"""
    练习2：定义函数,根据总两数,计算几斤零几两.:
     提示：使用容器包装需要返回的多个数据
    total_liang = int(input("请输入两:"))
    jin = total_liang // 16
    liang = total_liang % 16
    print(str(jin) + "斤零" + str(liang) + "两")
"""


def get_weight(total_liang):
    jin = total_liang // 16
    liang = total_liang % 16
    # 使用元组包装多个结果
    return jin, liang


# result = get_weight(100)
# print(result[0])
# print(result[1])

j, l = get_weight(100)
print(j)
print(l)
