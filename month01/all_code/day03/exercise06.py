"""
    练习5：
		根据心理年龄与实际年龄，打印智商等级。
	    智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
        天才：140以上（包含）
        超常：120-139之间（包含）
        聪慧：110-119之间（包含）
        正常：90-109之间（包含）
        迟钝：80-89之间（包含）
        低能：80以下
"""
ma = int(input("请输入心理年龄:"))
ca = int(input("请输入实际年龄:"))
iq = int(ma / ca * 100)
# 连续区间的范围判定:不必判断两边
if 140 <= iq:
    print("天才")
elif 120 <= iq:# 150
    print("超常")
elif 110 <= iq:
    print("聪慧")
elif 90 <= iq:
    print("正常")
elif 80 <= iq:
    print("迟钝")
else:
    print("低能")

# if iq >= 140:
#     print("天才")
#     # el 表达上面条件不满足(小于140)与iq < 140含义相同
# elif 120 <= iq < 140:
#     print("超常")
# elif 110 <= iq < 120:
#     print("聪慧")
# elif 90 <= iq < 110:
#     print("正常")
# elif 80 <= iq < 90:
#     print("迟钝")
# else:
#     print("低能")
