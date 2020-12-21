"""
    画出下列代码内存图
"""
data01 = 10
def func01():
    data01 = 20 # 修改全局变量

func01()

data02 = [10]
def func02():
    data02[0] = 20 # 读取全局变量,修改列表
func02()

print(data01) # ?
print(data02) # [20]

