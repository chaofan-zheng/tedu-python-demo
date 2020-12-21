# 练习2:在终端中录入多个人的身高,如果输入空字符串,
#       则停止录入. 再计算平均高度
# 注意:空字符串转换为整数,会报错.
sum_value = 0
count = 0
while True:
    height = input("请输入高度:")
    if height == "":
        break

    sum_value += int(height)
    count += 1
    
print("平均身高:" + str(sum_value / count))
