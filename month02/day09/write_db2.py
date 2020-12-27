"""
数据库写操作示例 2
"""
import pymysql

args = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8"
}

# 连接数据库
db = pymysql.connect(**args)

# 创建游标 游标对象：执行sql得到执行结果的对象
cur = db.cursor()

# 数据批量写操作 insert delete update
stu_list = [
    ("张三",18,'m',90),
    ("李四",19,'w',91),
    ("王五",20,'m',92)
]
try:
    sql = "insert into cls (name,age,sex,score) values (%s,%s,%s,%s);"
    cur.executemany(sql,stu_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭数据库连接
cur.close()
db.close()
