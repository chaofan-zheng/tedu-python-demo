"""
    lambda表达式
        定义：
            匿名函数
        语法：
            lambda 参数:函数体
        lambda能表达的函数,def都能表达.
        但是lambda函数体,不支持赋值语句,也只能有一条语句
"""
# 1. 有参数有返回值
# def func01(p1,p2):
#      return p1 > p2
func01 = lambda p1, p2: p1 > p2

print(func01(3, 8))

# 2. 有参数无返回值
# def func02(p1):
#     print("参数是:",p1)
func02 = lambda p1: print("参数是:", p1)

func02(250)


# 3. 无参数有返回值
# def func03():
#     return 250

func03 = lambda :250
print(func03())

# 4. 无参数无返回值
# def func04():
#     print("func04")

func04 = lambda :print("func04")
func04()

# 5. lambda 函数体,不支持赋值语句
def func05(p1):
    p1[0] = 100

# func05 = lambda p1: p1[0] = 100

list01 = [10]
func05(list01)
print(list01) # [100]

# 6. lambda 函数体,只能有一条语句
def func06():
    for i in range(5):
        print(i)

# func06 = lambda :for i in range(5):print(i)

func06()







