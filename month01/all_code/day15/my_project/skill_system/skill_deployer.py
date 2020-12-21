# 导入模块是否成功的唯一标准:
# 导入路径 + 系统路径 = 真实路径
import sys
sys.path.append("/home/tarena/month01/day15/my_project")
print(sys.path)



from common.list_helper import ListHelper

class SkillDeployer:
    def func02(self):
        print("func02")

ListHelper.func03()