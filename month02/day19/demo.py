
def login():
    while True:
        print("*** 查  询 ***")
        print("1) 查询单词")
        print("2) 历史记录")
        print("3) 注   销")
        print("")
        item = input("请输入选项:")
        if item == '1':
            pass
        elif item == '2':
            pass
        elif item == '3':
            break
        else:
            print("请输入正确选项！")


while True:
    print("*** 首  页 ***")
    print("1) 登  录")
    print("2) 注  册")
    print("3) 退  出")
    print("")
    item = input("请输入选项:")
    if item == '1':
        login()
    elif item == '2':
        pass
    elif item == '3':
        break
    else:
        print("请输入正确选项！")