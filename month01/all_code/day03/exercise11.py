"""
    练习2：
    	  在终端中显示0  1  2  3
          在终端中显示2  3  4  5  6
          在终端中显示1  3  5  7
          在终端中显示8  7  6  5  4
          在终端中显示-1  -2  -3  -4  -5
"""
count = 0
while count < 4:
    print(count)# 0 1 2 3
    count += 1

count = 2
while count < 7:
    print(count)# 2 3 4 5 6
    count += 1

count = 1
while count < 8:
    print(count)# 1  3  5  7
    count += 2

count = -1
while count > -6:
    print(count)# 8  7  6  5  4
    count -= 1



