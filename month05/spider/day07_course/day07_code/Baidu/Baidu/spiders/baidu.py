# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        """解析提取数据"""
        # response.xpath(): [<selector>,<selector>,....]
        # extract(): ['百度一下,你就知道']
        # extract_first(): '百度一下,你就知道'
        # get(): '百度一下,你就知道'
        r = response.xpath('/html/head/title/text()')
        print(r.extract())
        print(r.extract_first())
        print(r.get())
        # response的方法及属性
        html = response.text
        html = response.body







