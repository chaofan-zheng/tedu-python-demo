"""
库：noveldb
表：novel_tab
插入1条表记录
"""
import pymysql

# 创建2个对象(数据库连接对象、游标对象)
db = pymysql.connect(
    'localhost', 'root', '123456', 'noveldb', charset='utf8'
)
cur = db.cursor()
# 执行SQL命令,并提交到数据库执行
ins = 'insert into novel_tab values(%s,%s,%s,%s)'
cur.execute(ins, ('花千骨','http://a', '赵丽颖', '赵丽颖棒棒哒'))
db.commit()
# 关闭游标、断开数据库连接
cur.close()
db.close()











