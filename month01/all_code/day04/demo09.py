"""
    字符串格式化
        %d 整数
        %s 字符串
        %f 小数

        "......"%(变量)
"""
jin = 5
liang = 8
print("结果为：" + str(jin) + "斤" + str(liang) + "两")
print("结果为：%d斤%d两" % (jin, liang))

name = "悟空"
age = 6
score = 95.129
print("我是%s今年%.2d岁了,考试%.2f分." % (name, age, score))
