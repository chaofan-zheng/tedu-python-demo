"""
create database maoyandb charset utf8;
use maoyandb;
create table maoyantab(
name varchar(100),
star varchar(300),
time varchar(100)
)charset=utf8;
"""
import requests
import re
import time
import random
import pymysql

class MaoYanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
        self.db = pymysql.connect('localhost', 'root', '123456', 'maoyandb', charset='utf8')
        self.cur = self.db.cursor()

    def get_html(self, url):
        """请求"""
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        # r_list: [('名称','主演','上映时间'),(),(),(),(),(),(),(),(),()]
        r_list = re.findall(regex, html, re.S)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理"""
        ins = 'insert into maoyantab values(%s,%s,%s)'
        for r in r_list:
            self.cur.execute(ins, r)
            self.db.commit()
            print(r)

    def crawl(self):
        """爬虫逻辑函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(url=page_url)
            # 控制频率
            time.sleep(random.randint(1, 3))
        # 断开数据库
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    spider = MaoYanSpider()
    spider.crawl()




































