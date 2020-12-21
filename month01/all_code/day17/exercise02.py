# 练习：使用学生列表封装以下三个列表中数据
class Student:
    def __init__(self, name="", age=0, sex=""):
        self.name = name
        self.age = age
        self.sex = sex


list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]
list_student_sex = ["男", "男", "女"]

list_students = []
for item in zip(list_student_name, list_student_age, list_student_sex):
    # ('悟空', 28, '男') --> Student　对象
    # stu = Student(item[0],item[1],item[2])
    stu = Student(*item)
    list_students.append(stu)

# 通过调试查看列表中的数据
print(list_students)
