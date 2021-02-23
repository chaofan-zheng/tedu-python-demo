# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # 一级页面: 汽车名称、价格、链接
    title = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()
    # 二级页面: 里程、排量、变速箱
    km = scrapy.Field()
    displace = scrapy.Field()
    typ = scrapy.Field()



# 相当于: {'title':'', 'price':'', 'href':''}





