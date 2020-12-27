"""
数据库读操作示例
"""
import pymysql

args = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"stu",
    "charset":"utf8"
}

# 连接数据库
db = pymysql.connect(**args)

# 创建游标 游标对象：执行sql得到执行结果的对象
cur = db.cursor()

# 数据读操作  select
sql = "select name,score from cls " \
      "where score>%s;"
cur.execute(sql,[90])

# 迭代获取查询结果
# for row in cur:
#     print(row) # 一条记录

one = cur.fetchone() # 第一个记录
print(one)

many = cur.fetchmany(3) # 前3个记录
print(many)

all = cur.fetchall() # 所有记录
print(all)


# 关闭数据库连接
cur.close()
db.close()