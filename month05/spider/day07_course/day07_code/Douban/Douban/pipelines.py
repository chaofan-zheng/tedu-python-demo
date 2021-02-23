"""
create database doubandb charset utf8;
use doubandb;
create table doubantab(
rank int,
title varchar(100),
score decimal(3,1)
)charset=utf8;
"""

class DoubanPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))

        return item

import pymysql
class DoubanMysqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect('localhost', 'root', '123456', 'doubandb', charset='utf8')
        self.cur = self.db.cursor()
        self.ins = 'insert into doubantab values(%s,%s,%s)'

    def process_item(self, item, spider):
        li = [
            item['rank'],
            item['title'],
            item['score']
        ]
        self.cur.execute(self.ins, li)
        self.db.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()

import pymongo
class DoubanMongoPipeline(object):
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['doubandb']
        self.myset = self.db['doubanset']

    def process_item(self, item, spider):
        self.myset.insert_one(dict(item))
        return item










