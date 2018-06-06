# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item
class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.temp = None
        pass
        # self.file = open('submits.jl', 'w')

    def close_spider(self, spider):
        pass
        # self.file.close()

    def process_item(self, item_dict, spider):
        print("okokokokokokokokokokokokokok")
        page_num = int(item_dict['url_num'])/15
        file = open('submits-%d.jl'%(page_num), 'w')
        file.write(json.dumps(item_dict))
        file.close()
