from bll import EmployeeController
from model import EmployeeModel


class EmployeeView:

    def __init__(self):
        self.__controller = EmployeeController()

    def __display_menu(self):
        print("按1键录入员工信息")
        print("按2键显示员工信息")
        print("按3键删除员工信息")
        print("按4键修改员工信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_employee_info()
        elif item == "2":
            self.__display_employees()
        elif item == "3":
            self.__delete_employee()
        elif item == "4":
            self.__modify_employee()

    def __get_int(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("输入的不是整数")

    def __input_employee_info(self):
        emp = EmployeeModel()
        emp.name = input("请输入员工姓名:")
        emp.did = self.__get_int("请输入部门编号:")
        emp.money = self.__get_int("请输入员工薪资:")
        self.__controller.add_employee_info(emp)
        print("添加员工生成功喽")

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_employees(self):
        for item in self.__controller.list_employees:
            print(item)

    def __delete_employee(self):
        eid = self.__get_int("请输入需要删除的员工编号:")
        if self.__controller.remove_employee(eid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee(self):
        emp = EmployeeModel()
        emp.eid = self.__get_int("请输入员工编号:")
        emp.name = input("请输入员工姓名:")
        emp.did = self.__get_int("请输入部门编号:")
        emp.money = self.__get_int("请输入员工薪资:")
        if self.__controller.update_employee_info(emp):
            print("更新成功")
        else:
            print("更新失败")