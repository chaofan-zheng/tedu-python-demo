"""
    在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
"""

dict_color_info = {
    "R": "红色",
    "G": "绿色",
    "B": "蓝色",
    "A": "透明度"
}

color = input("请输入颜色(RGBA):")
# print(dict_color_info[color]) # 如果字典不存在当前key,会报错.
if color in dict_color_info:
    print(dict_color_info[color])
else:
    print("您输入的颜色不存在")
