"""
    # 练习2：遍历图形控制器
        略
"""
class GraphicController:
    pass

controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")

for item in controller:
    print(item)
