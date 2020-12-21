from bll import StudentController
from model import StudentModel

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

    def __get_int(self,message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("输入的不是整数")

    def __input_student_info(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        # stu.age = int(input("请输入学生年龄:"))
        stu.age = self.__get_int("请输入学生年龄:")
        # stu.score = int(input("请输入学生成绩:"))
        stu.score = self.__get_int("请输入学生成绩:")
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
        # sid = int(input("请输入需要删除的学生编号:"))
        sid = self.__get_int("请输入需要删除的学生编号:")
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        # stu.sid = int(input("请输入需要修改的学生编号:"))
        stu.sid = self.__get_int("请输入需要修改的学生编号:")
        stu.name = input("请输入需要修改的学生姓名:")
        stu.age = self.__get_int("请输入需要修改的学生年龄:")
        stu.score = self.__get_int("请输入需要修改的学生成绩:")
        if self.__controller.update_student_info(stu):
            print("更新成功")
        else:
            print("更新失败")