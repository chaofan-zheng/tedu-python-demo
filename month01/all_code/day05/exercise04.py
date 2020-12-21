"""
    列表基础操作-综合练习
    八大行星："水星" "金星" "地球" "火星" "木星" "土星" "天王星" "海王星"
        -- 创建列表存储4个行星："水星" "金星" "火星" "木星"
        -- 插入"地球"、追加"土星" "天王星" "海王星"
        -- 打印距离太阳最近、最远的行星(第一个和最后一个元素)
        -- 打印太阳到地球之间的行星(前两个行星)
        -- 删除"海王星",删除第四个行星
        -- 倒序打印所有行星(一行一个)
"""
list_planet = ["水星", "金星", "火星", "木星"]
list_planet.insert(2, "地球")
list_planet.append("土星")
list_planet.append("天王星")
list_planet.append("海王星")
# list_planet += ["土星","天王星","海王星"]
print(list_planet[0])
print(list_planet[-1])
print(list_planet[:2])
list_planet.remove("海王星")
del list_planet[3]

for i in range(len(list_planet) - 1, -1, -1):
    print(list_planet[i])
