"""
    猜数字游戏2.0版本
        增加:最多猜3次
            猜中提示:恭喜猜对了,总共猜了xx次
            否则提示:游戏失败
"""
import random

random_number = random.randint(1, 100)
count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入数字:"))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对了,总共猜了" + str(count) + "次")
        break
else:
    # 循环条件不满足才执行(break结束的循环不执行)
    print("游戏失败")