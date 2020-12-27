"""
练习2：
单词本： 每行一个单词
        单词和解释之间有空格
        后面的单词比前面的大
编写一个函数，传入一个单词
返回单词的对应解释
"""

def find_word(word:str)->str:
    """
    :param word: 要查找的单词
    :return: 得到的解释
    """
    file = open("dict.txt") # 打开
    # 每次回去一个单词
    for line in file:
        tmp = line.split(" ",1) # 按照空格分割
        # 如果迭代得到的单词已经比word大了就不用找了
        if tmp[0] > word:
            break
        elif word == tmp[0]:
            file.close()
            return tmp[1].strip()
    file.close()

print(find_word("aa"))

