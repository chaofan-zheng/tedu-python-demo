"""
    复习：
        函数式编程价值1：将函数(条件,处理)作为参数传递

"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    # 通过重写方法获取最值,只适用于最常见的条件
    # min(list_employees)
    # 如果条件过多,通过函数式编程实现.
    # 自定义函数(list_employees,lambda emp:emp.money
    def __lt__(self, other):
        return self.money < other.money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

min_value = IterableHelper.get_min(list_employees,lambda emp:emp.money)
print(min_value.__dict__)

min_value = min(list_employees)
print(min_value.__dict__)

