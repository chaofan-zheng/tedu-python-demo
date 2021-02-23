# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# 管道1: 功能就是终端打印输出汽车名字
class GuaziPipeline(object):
    def process_item(self, item, spider):
        print(item['title'])
        return item

# 管道2:将数据存入MySQL数据库
import pymysql
class GuaziMysqlPipeline(object):
    def open_spider(self, spider):
        """爬虫项目启动时,只执行1次,一般用于数据库连接"""
        print('天王盖地虎')
        self.db = pymysql.connect(
            'localhost','root','123456',
            'cardb',charset='utf8'
        )
        self.cur = self.db.cursor()
        self.ins = 'insert into cartab values(%s,%s,%s)'

    def process_item(self, item, spider):
        li = [
            item['title'],
            item['price'],
            item['href']
        ]
        self.cur.execute(self.ins, li)
        self.db.commit()

        return item

    def close_spider(self, spider):
        """爬虫项目结束时,只执行1次,一般用于数据库断开"""
        print('宝塔镇河妖')
        self.cur.close()
        self.db.close()

# 管道3:数据存入mongodb数据库
import pymongo

class GuaziMongoPipeline(object):
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(
            'localhost', 27017
        )
        self.db = self.conn['cardb']
        self.myset = self.db['carset']

    def process_item(self, item, spider):
        self.myset.insert_one(dict(item))

        return item














