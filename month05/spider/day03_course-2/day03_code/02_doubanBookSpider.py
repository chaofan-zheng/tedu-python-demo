"""
lxml + xpath 抓取豆瓣图书top250
"""
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent

class BookSpider:
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'


    def get_html(self, url):
        """请求+解析+数据处理"""
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """lxml + xpath解析提取数据"""
        # 1.创建解析对象
        eobj = etree.HTML(html)
        table_list = eobj.xpath('//table')
        for table in table_list:
            """书的信息要一个一个提取"""
            item = {}
            # 名称
            title_list = table.xpath('.//div[@class="pl2"]/a/@title')
            item['title'] = title_list[0] if title_list else None
            # 信息
            info_list = table.xpath('.//p[@class="pl"]/text()')
            item['info'] = info_list[0] if info_list else None
            # 评分
            score_list = table.xpath('.//span[@class="rating_nums"]/text()')
            item['score'] = score_list[0] if score_list else None
            # 评价人数
            commit_list = table.xpath('.//span[@class="pl"]/text()')
            item['commit'] = commit_list[0][1:-1].strip() if commit_list else None
            # 描述
            comment_list = table.xpath('.//span[@class="inq"]/text()')
            item['comment'] = comment_list[0] if comment_list else None
            print(item)

    def crawl(self):
        for page in range(1, 11):
            start = (page - 1) * 25
            page_url = self.url.format(start)
            self.get_html(url=page_url)
            # 控制数据抓取频率
            time.sleep(random.uniform(0, 2))

if __name__ == '__main__':
    spider = BookSpider()
    spider.crawl()
















