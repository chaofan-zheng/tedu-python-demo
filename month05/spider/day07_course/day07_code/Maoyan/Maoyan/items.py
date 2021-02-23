# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # 电影名称、主演、上映时间
    title = scrapy.Field()
    star = scrapy.Field()
    time = scrapy.Field()
