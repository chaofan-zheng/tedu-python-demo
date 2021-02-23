"""
瓜子二手车增量爬虫
一级页面：汽车链接(href)
二级页面：汽车名称(title)
要求：
   1、使用redis实现增量(新更新的汽车在页面的最前面)
   2、数据存入MongoDB数据库
"""
import requests
import re
import time
import random
import redis
import sys
import pymongo
from hashlib import md5

class GuaZiSpider:
    def __init__(self):
        self.url = 'https://www.guazi.com/nc/buy/o{}/#bread'
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Cookie': 'uuid=80480517-5cc9-4687-dd22-1df01a0fd096; ganji_uuid=1561931600173065002669; lg=1; user_city_id=214; antipas=8V16g5736871567349o772a8gR2; clueSourceCode=%2A%2300; sessionid=153bdd71-7120-4083-dfa8-a598e9ed9867; Hm_lvt_bf3ee5b290ce731c7a4ce7a617256354=1610677550,1612237012,1612343727,1612401513; close_finance_popup=2021-02-04; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2280480517-5cc9-4687-dd22-1df01a0fd096%22%2C%22ca_city%22%3A%22langfang%22%2C%22sessionid%22%3A%22153bdd71-7120-4083-dfa8-a598e9ed9867%22%7D; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A33550997015%7D; cityDomain=nc; preTime=%7B%22last%22%3A1612403484%2C%22this%22%3A1609990531%2C%22pre%22%3A1609990531%7D; Hm_lpvt_bf3ee5b290ce731c7a4ce7a617256354=1612403484',
        }
        # 连接Redis做增量爬虫
        self.r = redis.Redis(host='localhost', port=6379, db=0)
        # 连接MongoDB做数据持久化
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['guazidb']
        self.myset = self.db['guaziset']

    def get_html(self, url):
        """功能函数1：请求获取html"""
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8')

        return html

    def refunc(self, regex, html):
        """功能函数2：解析提取数据"""
        r_list = re.findall(regex, html, re.S)

        return r_list

    def md5_href(self, href):
        """功能函数3：生成指纹"""
        m = md5()
        m.update(href.encode())

        return m.hexdigest()

    def parse_html(self, first_url):
        """爬虫逻辑函数由此开始"""
        first_html = self.get_html(url=first_url)
        first_regex = '<li data-scroll-track=.*?href="(.*?)"'
        # href_list: ['/zz/...', '/zz/...', '', ...]
        href_list = self.refunc(first_regex, first_html)
        for href in href_list:
            finger = self.md5_href(href)
            if self.r.sadd("car:spiders", finger) == 1:
                # 开抓！
                self.get_car_info(href)
                # 控制频率
                time.sleep(random.randint(1, 2))
            else:
                sys.exit('更新完成')

    def get_car_info(self, href):
        """二级页面解析函数：提取汽车名字"""
        second_url = 'https://www.guazi.com' + href
        second_html = self.get_html(url=second_url)
        second_regex = '<h1 class="titlebox">(.*?)(?:<span class="labels">|</h1>)'
        # title_list: ['']
        title_list = self.refunc(second_regex, second_html)
        if title_list:
            item = {}
            item['title'] = title_list[0].strip()
            print(item)
            # 数据存入MongoDB数据库
            self.myset.insert_one(item)
        else:
            print('此辆汽车信息提取失败')

    def crawl(self):
        """程序入口函数"""
        for page in range(1, 2):
            page_url = self.url.format(page)
            self.parse_html(page_url)
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider = GuaZiSpider()
    spider.crawl()
































