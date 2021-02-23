# -*- coding: utf-8 -*-
import scrapy


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['www.so.com']
    start_urls = ['http://www.so.com/']

    def parse(self, response):
        r = response.xpath('/html/head/title/text()')
        print(r)
