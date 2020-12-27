"""
数据库的交互处理
"""
import pymysql


class Database:
    database_args = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "dict",
        "charset": "utf8"
    }

    def __init__(self):
        self.db = pymysql.connect(**Database.database_args)

    def course(self):
        self.cur = self.db.cursor()

    def close(self):
        self.db.close()

    def register(self, name, passwd):
        # 直接插入数据
        sql = "insert into user (name,passwd) values (%s,%s);"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self, name, passwd):
        sql = "select name from user where binary name=%s and binary passwd=%s;"
        self.cur.execute(sql, [name, passwd])
        if self.cur.fetchone():
            return True
        else:
            return False

    def query(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        # 查到：(mean,)  没查到：None
        mean = self.cur.fetchone()
        if mean:
            return mean[0]
        else:
            return "Not Found"

    def insert_hist(self, name, word):
        # hist --> id  word  time  user_id
        sql = "insert into hist (word,user_id) values (%s,(select id from user where name=%s));"
        try:
            self.cur.execute(sql, [word, name])
            self.db.commit()
        except Exception:
            self.db.rollback()

    def history(self, name):
        # name  word  time
        sql = "select user.name,hist.word,hist.time " \
              "from user left join hist " \
              "on user.id=hist.user_id " \
              "where user.name=%s " \
              "order by hist.time desc " \
              "limit 10;"
        self.cur.execute(sql, [name])
        return self.cur.fetchall()  # （（），（））
