# 在终端中累加 0  1  2  3
# 在终端中累加 2  3  4  5  6
# 在终端中累加 1  3  5  7
# 在终端中累加 8  7  6  5  4
# 在终端中累加 -1  -2  -3  -4  -5

result = 0
count = 0 # 开始0
while count < 4: # 3
    result += count
    count += 1# 0 1 2 3
print(result)

sum_value = 0
count = 2
while count < 7:
    sum_value += count
    count += 1
print(sum_value)

number = 0
count = 1
while count < 8:
    number += count
    count += 2
print(number)

number = 0
count = 8
while count >= 4:
    number += count
    count -= 1
print(number)

number = 0
count = -1
while count >= -5:
    number += count
    count -= 1
print(number)
