"""
    自定义迭代器
    需求:让for循环操作自定义对象
"""


class StudentIterator: # 迭代器:执行迭代过程
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]


class StudentController: # 可迭代对象:返回迭代器
    def __init__(self):
        self.__list_students = []

    def add_student(self, stu):
        self.__list_students.append(stu)

    def __iter__(self):
        return StudentIterator(self.__list_students)


if __name__ == '__main__':
    controller = StudentController()
    controller.add_student("孙浩")
    controller.add_student("陈小峰")
    controller.add_student("杨旭")
    # for item in controller:
    #     print(item)
    iterator = controller.__iter__()
    while True:
        try:
            item = iterator.__next__()
            print(item)  #
        except StopIteration:
            break
