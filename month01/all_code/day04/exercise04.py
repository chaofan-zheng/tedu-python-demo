# 练习1:在终端中录入5个人的身高,计算平均高度
sum_value = 0
for item in range(5):# 0 1 2 3 4
    sum_value += int(input("请输入身高:"))
print("平均身高:"+str(sum_value / 5))

