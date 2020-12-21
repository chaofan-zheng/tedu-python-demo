"""
    练习：将下列英文语句按照单词进行翻转.
    转换前：To have a government that is of people by people for people
    转换后：people for people by people of is that government a have To
"""
message = "To have a government that is of people by people for people"
list_datas = message.split(" ")
message = " ".join(list_datas[::-1])
print(message)