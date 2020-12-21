"""
    练习3：多个人的多个爱好
    dict_hobbies = {
        "于谦": ["抽烟", "喝酒", "烫头"],
        "郭德纲": ["说", "学", "逗", "唱"],
    }
    1.	打印于谦的所有爱好(一行一个)
    效果：抽烟
          喝酒
    烫头
    2.	计算郭德纲所有爱好数量
    效果：4
    3.	打印所有人(一行一个)
    效果：于谦
          郭德纲
    4.	打印所有爱好(一行一个)
    抽烟
    喝酒
    烫头
    说
    学
    逗
    唱
"""
dict_hobbies = {
    "于谦": ["抽烟", "喝酒", "烫头"],
    "郭德纲": ["说", "学", "逗", "唱"],
}
# 1. 打印于谦的所有爱好(一行一个)
for item in dict_hobbies["于谦"]:
    print(item)
# 2. 计算郭德纲所有爱好数量
print(len(dict_hobbies["郭德纲"]))
# 3. 打印所有人(一行一个)
for key in dict_hobbies:
    print(key)
# 4. 打印所有爱好(一行一个)
for value in dict_hobbies.values():
    for item in value:
        print(item)
