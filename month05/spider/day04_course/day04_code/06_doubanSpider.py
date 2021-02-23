"""
抓取豆瓣电影排行榜
在此代码基础上做如下扩展:
1、自动抓取剧情类别下的所有电影(获取电影总数)
2、抓取所有类别的所有电影
   运行效果如下
      请输入电影类别(剧情|喜剧|动作|爱情|....)：爱情
      结果：抓取爱情类别下的所有电影
"""
import requests
import json
import time
import random
from fake_useragent import UserAgent

class DouBanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'

    def get_html(self, url):
        """请求功能函数"""
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url, headers=headers).text

        return html

    def parse_html(self, url):
        """爬虫逻辑函数"""
        html = self.get_html(url=url)
        # html: [{},{},...{}]
        html = json.loads(html)
        for one_film_dict in html:
            item = {}
            item['rank'] = one_film_dict['rank']
            item['title'] = one_film_dict['title']
            item['score'] = one_film_dict['score']
            item['time'] = one_film_dict['release_date']
            print(item)

    def crawl(self):
        for start in range(0, 101, 20):
            page_url = self.url.format(start)
            self.parse_html(url=page_url)
            # 控制频率
            time.sleep(random.uniform(0, 1))

if __name__ == '__main__':
    spider = DouBanSpider()
    spider.crawl()














