"""
    餐厅架构
        迎宾 -- 点餐服务员 -- 厨师 -- 送菜服务员
    软件架构
        视图View                控制Controller
            界面逻辑(输入输出)        业务逻辑(核心算法)

                    模型Model
                        数据抽象

    练习:参照学生信息管理系统,实现商品信息管理系统
        (1)录入商品信息
            class Commodity:
                def __init__(self, cid=0, name="", price=0):
                    self.cid = cid  # 商品编号
                    self.name = name
                    self.price = price
        (2)存储商品信息,显示信息
        (3)删除商品信息
        (4)修改商品信息
"""

class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 编号(对学生信息的唯一标记)
        self.sid = sid

    def __str__(self):  # 对象 -> 字符串
        return "我是%s,学号是%d,今年%d岁了,考试%d分" % (self.name, self.sid, self.age, self.score)

    # 指定比较相同的依据
    def __eq__(self, other):
        return self.sid == other.sid

class StudentView:
    """
        学生视图类
    """

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            # 自动生成参数/函数:alt + 回车
            self.__input_student_info()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def __input_student_info(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        self.__controller.add_student_info(stu)
        print("添加学生成功喽")

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_students(self):
        for item in self.__controller.list_students:
            print(item)

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号:"))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入需要修改的学生编号:"))
        stu.name = input("请输入需要修改的学生姓名:")
        stu.age = int(input("请输入需要修改的学生年龄:"))
        stu.score = int(input("请输入需要修改的学生成绩:"))
        if self.__controller.update_student_info(stu):
            print("更新成功")
        else:
            print("更新失败")

class StudentController:
    """
        学生信息的控制
    """

    def __init__(self):
        self.__list_students = []
        self.__start_id = 1001  # 开始编号

    # 只读属性
    @property
    def list_students(self):
        return self.__list_students

    def add_student_info(self, stu_target):
        """
            添加学生信息
        :param stu_target: 从view中准备好的学生信息
        """
        stu_target.sid = self.__start_id
        self.__start_id += 1
        self.__list_students.append(stu_target)

    def remove_student(self, sid):
        """
            删除学生信息
        :param sid: 需要删除的学生编号
        :return: 是否删除成功
        """
        stu = StudentModel(sid=sid)
        if stu in self.__list_students:
            # remove 如果删除不存在的数据会报错
            self.__list_students.remove(stu)
            return True  # 删除成功
        else:
            return False  # 删除失败

    def update_student_info(self, new_stu):
        """
            修改学生信息
        :param new_stu:新学生信息
        :return: 是否修改成功
        """
        for item in self.__list_students:
            if item.sid == new_stu.sid:
                # item.name = new_stu.name
                # item.age = new_stu.age
                # item.score = new_stu.score
                item.__dict__ = new_stu.__dict__
                return True  # 修改成功
        return False  # 修改失败

# 入口
view = StudentView()
view.main()
