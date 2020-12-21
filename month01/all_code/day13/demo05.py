"""
    员工管理器2.0
"""


# ---------------搭建架构--------------------

class EmployeeManager:
    """
        员工管理器
    """

    def __init__(self):
        self.__all_employee = []

    def get_total_salary(self):
        total_salary = 0
        for item in self.__all_employee:
            # 编码时 调用 父方法
            # 运行时 执行 子方法
            total_salary += item.calculate_salary()
        return total_salary

    def add_employee(self, emp):
        self.__all_employee.append(emp)


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

# ----------------填充具体功能-------------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.base_salary + self.bonus
        return super().calculate_salary() + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() + self.bug_count * 5


# ----------------入口代码-------------------
manager = EmployeeManager()
manager.add_employee(Programmer(10000, 1000000))
manager.add_employee(Tester(8000, 500))
total_salary = manager.get_total_salary()
print(total_salary)
