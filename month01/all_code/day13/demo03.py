"""
    需求:
        创建员工管理器
        -- 存储很多员工
        -- 计算所有员工总薪资
    岗位:
        程序员:底薪 + 项目分红
        测试员:底薪 + Bug数*5元
    要求:
        增加新岗位,员工管理器不变.
    设计:
        封装(分):创建员工管理器类/程序员类/测试员类
        继承(隔):创建岗位类,隔离员工管理器类与具体岗位(程序员类/测试员类)与的变化
        多态(做):具体岗位(程序员类/测试员类)重写岗位类的计算薪资方法,以实现具体功能
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
        if isinstance(emp,Employee):
            self.__all_employee.append(emp)


class Employee:
    def calculate_salary(self):
        pass


# ----------------填充具体功能-------------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def calculate_salary(self):
        return self.base_salary + self.bug_count * 5


# ----------------入口代码-------------------
manager = EmployeeManager()
manager.add_employee(Programmer(10000, 1000000))
manager.add_employee(Tester(8000, 500))
manager.add_employee("xxx")
total_salary = manager.get_total_salary()
print(total_salary)
