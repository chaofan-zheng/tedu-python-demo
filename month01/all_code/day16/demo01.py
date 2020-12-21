"""
    异常处理
        1. 目标:解决程序运行时的逻辑错误(数据超过有效范围).
               不负责处理语法错误.
        2. 现象:程序不再向下执行,而是不断向上返回.
        3. 目的:将异常流程(向上),恢复为正常流程(向下).
        4. 手段:四种写法
        5. 价值:
            保障程序可以按照既定的流程执行
            就近原则
            A --> B --> C --> D --> E --> ...
"""


# 1. 语法错误
# class MyClass:
#     pass
#
# m01 = MyClass()
# print(m01.name)# AttributeError

# print(qtx) # NameError

# 2. 逻辑错误
# def div_apple(apple_count):
#     # 如果发生异常,返回给调用者
#     person_count = int(input("请输入人数:")) # ValueError
#     result = apple_count / person_count # ZeroDivisionError
#     print(f"每个人分了{result}个苹果")
#
# def main():
#     div_apple(10)
#
# main()
# print("后续逻辑")

# 写法1:"包治百病"
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))  # ValueError
#         result = apple_count / person_count  # ZeroDivisionError
#         print(f"每个人分了{result}个苹果")
#     # except Exception:
#     except:
#         print("出错啦") # 程序能够执行本行,说明个程序已经恢复正常
#
# div_apple(10)

# 写法2:"对症下药" (官方建议)
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))  # ValueError
#         result = apple_count / person_count  # ZeroDivisionError
#         print(f"每个人分了{result}个苹果")
#     except ValueError:
#         print("输入的不是整数")
#     except ZeroDivisionError:
#         print("输入的是零")
#
# div_apple(10)

# 3. 写法3:无论对错,无论处理与否,一定执行某些逻辑.
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))  # ValueError
#         result = apple_count / person_count  # ZeroDivisionError
#         print(f"每个人分了{result}个苹果")
#         # 文件处理
#         # 1. 打开文件(开门)
#         # 2. 处理逻辑(进入房间)
#     finally:
#         # 3. 关闭文件(关门)
#         print("分苹果结束啦")
#
# div_apple(10)

# 写法4:程序没有出错执行的逻辑
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))  # ValueError
        result = apple_count / person_count  # ZeroDivisionError
        print(f"每个人分了{result}个苹果")
    except:
        print("分苹果失败啦")
    else:  # 与except互斥
        print("分苹果成功啦")

div_apple(10)
print("后续逻辑")
