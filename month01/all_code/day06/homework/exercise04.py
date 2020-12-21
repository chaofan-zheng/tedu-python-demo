"""
    计算给定字符串列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
    字符串列表：words =["qtx","看一看","想啊想","练练"]
"""
words =["qtx","看一看","想啊想","练练"]
counter = 0
for word in words:
    if len(word) > 2 and word[0] == word[-1]:
        counter += 1
print(counter)