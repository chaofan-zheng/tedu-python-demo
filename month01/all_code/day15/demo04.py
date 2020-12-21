"""
    (仅作了解)
    包中的__init__模块作用
        当所在包被导入时,自动执行__init__.py模块
        可以提供可导出成员
"""
# import 包
import package01.package02 as p2

p2.xxx()
p2.module02.func01()
p2.func01()

# from 包 import 包
from package01 import package02

package02.xxx()
package02.module02.func01()
package02.func01()



