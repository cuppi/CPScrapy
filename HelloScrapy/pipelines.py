# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from .items import JDFirstCategoryItem, JDSecondCategoryItem, JDThirdCategoryItem
from util.category_manager import CategoryManager


class HelloscrapyPipeline(object):

    def __init__(self):
        self.categoryList = []
        self.file = codecs.open(
            'jd_category_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.categoryList.append(item)
        return item

    # 对象转换成dict
    def obj2dict(self, obj):
        if isinstance(obj, JDFirstCategoryItem) or isinstance(obj, JDSecondCategoryItem):
            return dict({'name': obj['name'], 'categoryList': obj['categoryList']})
        return dict(obj)

    def close_spider(self, spider):
        item = CategoryManager.default_manager(CategoryManager).insert_item(self.categoryList)
        # self.file.write(json.dumps(self.categoryList,
        #                            default=self.obj2dict,
        #                            indent=1,
        #                            sort_keys=False,
        #                            ensure_ascii=False))
        # self.file.close()
