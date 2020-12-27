"""
数据库写操作示例
1. 使用pymysql写数据库会自动开启事务
2. 如果引擎不支持事务则execute后直接生效
3. 如果引擎支持事务则需要commit后才生效
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

# 数据写操作 insert delete update
try:
    sql = "update cls set score=%s where name=%s;"
    cur.execute(sql,[99,"Lily"])
    db.commit()  # 统一提交写操作
except Exception as e:
    print(e)
    db.rollback() # 回滚

# 关闭数据库连接
cur.close()
db.close()
