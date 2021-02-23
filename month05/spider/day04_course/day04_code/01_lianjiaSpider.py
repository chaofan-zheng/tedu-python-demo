"""
链家二手房数据抓取
"""
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
import pymongo

class LianJiaSpider:
    def __init__(self):
        self.url = 'https://lf.lianjia.com/ershoufang/pg{}/'
        # 3个对象
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['lianjiadb']
        self.myset = self.db['lianjiaset']

    def get_html(self, url):
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        eobj = etree.HTML(html)
        li_list = eobj.xpath('//ul/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        for li in li_list:
            item = {}
            name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item['name'] = name_list[0] if name_list else None

            address_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['address'] = address_list[0] if address_list else None

            info_list = li.xpath('.//div[@class="houseInfo"]/text()')
            item['info'] = info_list[0] if info_list else None

            total_list = li.xpath('.//div[@class="totalPrice"]/span/text()')
            item['total'] = total_list[0] if total_list else None

            unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit'] = unit_list[0] if unit_list else None

            print(item)
            self.myset.insert_one(item)

    def crawl(self):
        for page in range(1, 101):
            page_url = self.url.format(page)
            self.get_html(url=page_url)
            # 控制数据抓取的频率
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider = LianJiaSpider()
    spider.crawl()























