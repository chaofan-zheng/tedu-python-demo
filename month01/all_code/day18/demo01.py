"""
    内置高阶函数与自定义的集成操作框架IterableHelper对比：
        从功能角度讲：集成操作框架更完善
                    (在后续编程生涯中,需要不断增加新的通用功能)
        从教学角度讲：深刻体会函数式编程思想(分隔做)
        从面试角度讲：在简历中添加“精通函数式编程”
        从性能角度讲：内置高阶函数更快
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
    Employee(1001, 9002, "师父", 60000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# 需求：获取所员工的员工编号
for item in IterableHelper.select(list_employees, lambda item: item.eid):
    print(item)

# 1. map映射：
for item in map(lambda item: item.eid, list_employees):
    print(item)

# 需求：获取部门编号是9001的所有员工
for item in IterableHelper.find_all(list_employees, lambda emp: emp.did == 9001):
    print(item.__dict__)

# 2. filter过滤：
for item in filter(lambda emp: emp.did == 9001, list_employees):
    print(item.__dict__)

max_value = IterableHelper.get_max(list_employees, lambda element: element.money)
print(max_value.__dict__)

# 3.max 最大  min 最小
max_value = max(list_employees, key=lambda element: element.money)
print(max_value.__dict__)

# 4.
# 自定义排序函数内部修改了列表,所以没有提供返回值
# IterableHelper.order_by(list_employees,lambda item:item.did)
# print(list_employees)

# 内置sorted排序,返回排好序的新列表
# 升序
new_list = sorted(list_employees, key=lambda item: item.did)
# 降序 reverse=True
new_list = sorted(list_employees, key=lambda item: item.did, reverse=True)
print(new_list)
