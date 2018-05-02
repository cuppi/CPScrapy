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
            'jd_category_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.categoryList.append(item)
        return item

    def close_spider(self, spider):
        first_dict = {}
        for first_category in self.categoryList:
            second_category_list = []
            for second_category in first_category['secondCategoryList']:
                third_category_list = []
                for third_category in second_category['thirdCategoryList']:
                    third_category_list.append({'name': third_category['name']})
                second_category_list.append({second_category['name']: third_category_list})
            first_dict[first_category['name']] = second_category_list
        print(self.categoryList)
        self.file.write(json.dumps(first_dict,
                                   indent=1,
                                   sort_keys=False,
                                   ensure_ascii=False))
        self.file.close()
