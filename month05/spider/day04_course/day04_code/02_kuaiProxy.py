"""
create database proxydb charset utf8;
use proxydb;
create table proxytab(
ip varchar(50),
port varchar(10)
)charset=utf8;
"""

import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
import pymysql

class KuaiProxy:
    def __init__(self):
        self.url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.test_url = 'http://httpbin.org/get'
        self.headers = {'User-Agent':UserAgent().random}
        self.db = pymysql.connect('localhost', 'root', '123456', 'proxydb', charset='utf8')
        self.cur = self.db.cursor()

    def get_proxy(self, url):
        html = requests.get(url=url, headers=self.headers).text
        # lxml+xpath解析提取数据
        eobj = etree.HTML(html)
        tr_list = eobj.xpath('//table/tbody/tr')
        for tr in tr_list:
            ip = tr.xpath('./td[1]/text()')[0]
            port = tr.xpath('./td[2]/text()')[0]
            # 测试此ip和port是否可用
            self.test_proxy(ip, port)

    def test_proxy(self, ip, port):
        """测试1个ip和port是否可用"""
        proxies = {
            'http' : 'http://{}:{}'.format(ip, port),
            'https' : 'https://{}:{}'.format(ip, port),
        }
        try:
            resp = requests.get(url=self.test_url,
                                proxies=proxies,
                                headers=self.headers,
                                timeout=3)
            print(ip, port, '\033[31m可用\033[0m')
            ins = 'insert into proxytab values(%s,%s)'
            self.cur.execute(ins, [ip, port])
            self.db.commit()
        except Exception as e:
            print(ip, port, '不可用')

    def crawl(self):
        for page in range(1, 1001):
            page_url = self.url.format(page)
            self.get_proxy(url=page_url)
            time.sleep(random.uniform(0, 2))

if __name__ == '__main__':
    spider = KuaiProxy()
    spider.crawl()























