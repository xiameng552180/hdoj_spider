# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SubmitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time = scrapy.Field()
    judgeStatus = scrapy.Field()
    problemID = scrapy.Field()
    executeTime = scrapy.Field()
    executeMemory = scrapy.Field()
    codeLength = scrapy.Field()
    language = scrapy.Field()
    author = scrapy.Field()
    page = scrapy.Field()
    pass

class ItemList(scrapy.Item):
    pass