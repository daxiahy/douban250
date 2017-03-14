# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影名字
    title=scrapy.Field()
    #电影介绍
    movieInfo=scrapy.Field()
    #电影星级
    star=scrapy.Field()
    #电影台词
    quote=scrapy.Field()
    #电影地址
    url=scrapy.Field()
