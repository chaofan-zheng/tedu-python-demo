# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def parse(self, response):
        """提取数据"""
        dd_list = response.xpath('//dl/dd')
        for dd in dd_list:
            item = MaoyanItem()
            item['title'] = dd.xpath('.//p[@class="name"]/a/@title').get()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get()

            # 交给项目管道文件处理
            yield item






