"""
    复习 - MVC
"""

class XXView:
    def __init__(self):
        # 桥：连接了V 与 C
        self.__controller = XXXController()

    def func01(self):
        self.__controller.func02()

class XXXController:
    def func02(self):
        pass
