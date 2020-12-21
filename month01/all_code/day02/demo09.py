"""
    增强运算符(累计运算)：
        在算数运算符基础上,增加对变量自身赋值的功能
        +=  -=  *=  /=   //=   %=   **=
    练习:exercise09

"""
number = 10
number + 5 # 不会影响变量number
print(number)  # 10

number = 10
# number = number + 5 # 累加
number += 5
print(number)  # 15
