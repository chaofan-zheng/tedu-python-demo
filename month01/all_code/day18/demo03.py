"""
    闭包-语法
        步骤：
            1. 有外有内
            2. 内使用外
            3. 外返回内
        作用：外部函数栈帧执行过后不释放,
             留着给内部函数反复使用.
        字面意思：封闭  内存空间
"""


def func01():
    a = 100

    def func02():
        print(a)

    return func02


# 调用外部函数,接收内部函数
result = func01()
# 反复调用内部函数
result()
result()
result()
