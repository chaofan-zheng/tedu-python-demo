from model import EmployeeModel


class EmployeeController:

    def __init__(self):
        self.__list_employees = []
        self.__start_id = 1001  # 开始编号

    # 只读属性
    @property
    def list_employees(self):
        return self.__list_employees

    def add_employee_info(self, emp_target):
        emp_target.eid = self.__start_id
        self.__start_id += 1
        self.__list_employees.append(emp_target)

    def remove_employee(self, eid):
        emp = EmployeeModel(eid)
        if emp in self.__list_employees:
            self.__list_employees.remove(emp)
            return True
        else:
            return False

    def update_employee_info(self, new_emp):
        for item in self.__list_employees:
            if item.eid == new_emp.eid:
                item.__dict__ = new_emp.__dict__
                return True
        return False
