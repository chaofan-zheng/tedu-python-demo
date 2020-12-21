"""
    练习：
        循环录入编码值打印文字，直到输入空字符串停止。
        效果：
        请输入数字：113
        q
        请输入数字：116
        t
        请输入数字：
        Process finished with exit code 0
"""
while True:
    code_value = input("请输入编码值:")
    if code_value == "":
        break
    print(chr(int(code_value)))