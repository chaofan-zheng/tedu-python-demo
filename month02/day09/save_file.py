"""
文件存储到数据库
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
cur = db.cursor()

# 插入图片
# with open("timg.jfif",'rb') as f:
#     data = f.read()
# try:
#     sql = "update cls set image=%s where id=2;"
#     cur.execute(sql,[data])
#     db.commit()  # 统一提交写操作
# except Exception as e:
#     print(e)
#     db.rollback() # 回滚

# 关闭数据库连接

# 获取图片
sql = "select image from cls " \
      "where id=2;"
cur.execute(sql)

# data是图片内容
data = cur.fetchone()[0]
with open("kb.jpg",'wb') as f:
    f.write(data)

cur.close()
db.close()
