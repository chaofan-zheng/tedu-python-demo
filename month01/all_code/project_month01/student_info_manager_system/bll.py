from model import StudentModel


class StudentController:
    """
        学生信息的控制
    """

    def __init__(self):
        self.__list_students = []
        self.__start_id = 1001  # 开始编号

    # 只读属性
    @property
    def list_students(self):
        return self.__list_students

    def add_student_info(self, stu_target):
        """
            添加学生信息
        :param stu_target: 从view中准备好的学生信息
        """
        stu_target.sid = self.__start_id
        self.__start_id += 1
        self.__list_students.append(stu_target)

    def remove_student(self, sid):
        """
            删除学生信息
        :param sid: 需要删除的学生编号
        :return: 是否删除成功
        """
        stu = StudentModel(sid=sid)
        if stu in self.__list_students:
            # remove 如果删除不存在的数据会报错
            self.__list_students.remove(stu)
            return True  # 删除成功
        else:
            return False  # 删除失败

    def update_student_info(self, new_stu):
        """
            修改学生信息
        :param new_stu:新学生信息
        :return: 是否修改成功
        """
        for item in self.__list_students:
            if item.sid == new_stu.sid:
                # item.name = new_stu.name
                # item.age = new_stu.age
                # item.score = new_stu.score
                item.__dict__ = new_stu.__dict__
                return True  # 修改成功
        return False  # 修改失败

if __name__ == '__main__':
    # 测试代码
    controller = StudentController()
    controller.add_student_info(StudentModel())
    controller.add_student_info(StudentModel())
    for item in controller.list_students:
        print(item)

