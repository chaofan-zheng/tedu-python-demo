# -*- coding: utf-8 -*-
import json
from ..items import DoubanItem
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'

    def start_requests(self):
        """生成所有要抓取的URL地址,交给调度器入队列"""
        for start in range(0, 101, 20):
            page_url = self.url.format(start)
            # 交给调度器入队列
            yield scrapy.Request(url=page_url,
                                 callback=self.parse)


    def parse(self, response):
        """解析提取数据"""
        html = json.loads(response.text)
        for one_dict in html:
            item = DoubanItem()
            item['rank'] = one_dict['rank']
            item['title'] = one_dict['title']
            item['score'] = one_dict['score']

            # 交给项目管道处理
            yield item








