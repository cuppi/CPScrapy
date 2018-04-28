# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class HelloscrapyPipeline(object):

    def __init__(self):
        # self.file = open('data.json', 'wb')
        self.categoryList = []
        self.file = codecs.open(
            'jd_category_utf81.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.categoryList.append(item)
        return item

    def close_spider(self, spider):
        categoryDict = {}
        for category in self.categoryList:
            parentName = category['parentName']
            if parentName in categoryDict:
                categoryDict[parentName].append(dict({'name': category['name']}))
            else:
                categoryDict[parentName] = [dict({'name': category['name']})]
        self.file.write(json.dumps(categoryDict,
                                   indent=1,
                                   sort_keys=False,
                                   ensure_ascii=False))
        self.file.close()
