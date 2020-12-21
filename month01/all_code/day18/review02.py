"""
    复习
        函数式编程思想
            适用性：多个函数主体结构相同,核心算法不同.
            分：将主体结构与核心算法封装到单独函数中
            隔：在主体结构中使用参数抽象核心算法
            做：通过lambda表达式完成核心算法
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
"""
def get_count01():
    count = 0
    for item in list_employees:
        if item.money > 20000:
            count += 1
    return count

def get_count02():
    count = 0
    for item in list_employees:
        if item.did == 9002:
            count += 1
    return count

value  = get_count02()
print(value)

# 分 - 变化
# 火车
def condition01(item):
    return item.money > 20000

# 汽车
def condition02(item):
    return item.did == 9002

# 分 - 不变
def get_count(func):
    count = 0
    for item in list_employees:
        # if item.did == 9002:
        # if condition02(item):
        # if condition01(item):
        # 先确定用法
        if func(item):
            count += 1
    return count
"""

value = IterableHelper.get_count(list_employees,lambda item:item.money > 20000)
print(value)

IterableHelper.order_by(list_employees,lambda item:item.money)
print(list_employees)