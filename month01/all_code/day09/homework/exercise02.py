"""
    创建函数,打印所有员工信息
    创建函数,打印所有月薪大于2w的员工信息,
    创建函数,在部门列表中查找编号最小的部门
    创建函数,根据部门编号对部门列表升序排列
"""

# 员工列表(员工编号 部门编号 姓名 工资)
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]

def print_single_employee(eid, emp):
    print(f"{emp['name']}的员工编号是{eid},部门编号是{emp['did']},月薪{emp['money']}元.")

# 1. 打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_all_employees():
    for eid, emp in dict_employees.items():
        print_single_employee(eid, emp)

# 2. 打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_gt_2w_employees():
    for eid, emp in dict_employees.items():
        if emp['money'] > 20000:
            print_single_employee(eid, emp)

# 3. 在部门列表中查找编号最小的部门
def get_min_by_did():
    min_value = list_departments[0]
    for i in range(1, len(list_departments)):
        if min_value["did"] > list_departments[i]["did"]:
            min_value = list_departments[i]
    return min_value

# 4. 根据部门编号对部门列表升序排列
def order_by_did():
    # (1)取
    for r in range(len(list_departments) - 1):
        # (2)比
        for c in range(r + 1, len(list_departments)):
            # (3) 发现更小
            if list_departments[r]["did"] > list_departments[c]["did"]:
                # (4) 交换
                list_departments[r], list_departments[c] = list_departments[c], list_departments[r]


# 测试
print_all_employees()
print_gt_2w_employees()
result = get_min_by_did()
print(result)

order_by_did()
print(list_departments)
