"""
    练习:调用module_exercise中成员
"""
# 方式1:"我过去"
# 适用性: 适合面向过程的技术(全局变量/函数)
import module_exercise # 执行module_exercise中的代码

print(module_exercise.data)
module_exercise.func01()
# 通过对象调用实例方法
m01 = module_exercise.MyClass()
m01.func02()
# 通过类名调用类方法
module_exercise.MyClass.func03()


# 方式2:"你过来"
# 适用性: 适合面向对象的技术(类)
from module_exercise import *

print(data)
func01()
m02 = MyClass()
m02.func02()
MyClass.func03()





