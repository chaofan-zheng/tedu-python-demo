# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名,用于运行爬虫 scrapy crawl 爬虫名
    name = 'baidu'
    # 允许抓取的域名
    allowed_domains = ['www.baidu.com']
    # 起始的URL地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # response: http://www.baidu.com/的响应对象
        r = response.xpath('/html/head/title/text()')
        print(r)
