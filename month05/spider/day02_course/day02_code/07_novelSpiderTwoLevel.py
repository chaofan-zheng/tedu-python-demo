"""
两级页面数据抓取
"""
import requests
import re
import time
import random
import pymongo

class NovelSpider:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
        # 3个对象
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['noveldb']
        self.myset = self.db['novelset2']

    def get_html(self, url):
        """功能函数1：发请求获取响应内容html"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def refunc(self, regex, html):
        """功能函数2：正则解析功能函数"""
        r_list = re.findall(regex, html, re.S)

        return r_list

    def parse_html(self, first_url):
        """爬虫逻辑由此开始"""
        first_html = self.get_html(url=first_url)
        first_regex = '<div class="caption">.*?href="(.*?)" title="(.*?)">.*?<small class="text-muted fs-12">(.*?)</small>.*?>(.*?)</p>'
        first_list = self.refunc(first_regex, first_html)
        for first in first_list:
            item = {}
            item['href'] = first[0]
            item['title'] = first[1]
            item['author'] = first[2]
            item['comment'] = first[3]
            # 继续向item['href']发请求,获取详情页的数据
            self.get_novel_info(item)
            # 控制数据抓取的频率
            time.sleep(random.uniform(0, 2))

    def get_novel_info(self, item):
        """二级页面解析函数：最新章节名称+链接"""
        second_html = self.get_html(url=item['href'])
        second_regex = '<dd class="col-md-4"><a href="(.*?)">(.*?)</a></dd>'
        second_list = self.refunc(second_regex, second_html)
        for second in second_list:
            one_chapter_dict = {}
            one_chapter_dict['chapter_name'] = second[1]
            one_chapter_dict['chapter_href'] = second[0]
            one_chapter_dict['href'] = item['href']
            one_chapter_dict['title'] = item['title']
            one_chapter_dict['author'] = item['author']
            one_chapter_dict['comment'] = item['comment']
            print(one_chapter_dict)
            # 数据存入mongodb数据库
            self.myset.insert_one(one_chapter_dict)

    def crawl(self):
        """逻辑函数"""
        for page in range(1, 3):
            page_url = self.url.format(page)
            self.parse_html(page_url)

if __name__ == '__main__':
    spider = NovelSpider()
    spider.crawl()





































