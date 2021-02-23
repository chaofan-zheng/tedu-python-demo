# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # 排名、名称、评分
    rank = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()








