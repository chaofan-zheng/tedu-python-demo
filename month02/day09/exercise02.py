"""
练习2：
创建数据库 dict
create database dict charset=utf8;
在其中创建一个数据表 words
id  word   mean

create table words (id int primary key auto_increment,word char(30),mean varchar(256));

编写一个程序将dict.txt文本的单词存入该数据表
"""
import pymysql
import re

args = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}


# 获取我要插入的数据
def get_data(filename):
    """
    :param filename: 单词本文件
    :return: 可插入数据
    """
    data = []  # 装单词 [(word,mean),()....]
    file = open(filename)
    for line in file:
        word = re.findall(r"(\w+)\s+(.*)", line)
        data.append(word[0])
    file.close()
    return data  # 要插入的单词


def main():
    # 连接数据库
    db = pymysql.connect(**args)
    cur = db.cursor()
    # 调用get_data获取数据
    data = get_data("dict.txt")
    try:
        sql = "insert into words (word,mean) values (%s,%s);"
        cur.executemany(sql, data)
        db.commit()
    except:
        db.rollback()

    # 关闭数据库连接
    cur.close()
    db.close()


if __name__ == '__main__':
    main()
