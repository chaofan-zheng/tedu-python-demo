"""
    练习:
    在终端中输入任意整数，计算累加和.
    "1234" -> "1" -> 累加 1
    效果：
        请输入一个整数:12345
        累加和是 15
"""
number = input("请输入数字:") # "1234"
sum_value = 0
for item in number: # "1"  "2"  "3"  "4"
    sum_value += int(item)
print("累加和是:"+str(sum_value))