"""
    软件架构
        View:界面逻辑,例如:负责输入输出
        Model:数据的抽象,例如:学生类型(姓名,年龄,成绩...)
        Controller:核心业务逻辑,例如:存储,编号
"""


class View:
    def __init__(self):
        self.controller = Controller()

    def func01(self):
        self.controller.func02()

class Controller:
    def func02(self):
        print("func02执行了")

view = View()
view.func01()
