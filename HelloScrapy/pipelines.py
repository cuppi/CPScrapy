# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

mongo_uri = 'mongodb://localhost:27017/'
mongo_db = 'jd_scrapy_data'
collection_name = 'category_collection'


class HelloscrapyPipeline(object):
    def __init__(self):
        self.client: MongoClient = None
        self.db: Database = None
        self.categoryList = []
        self.file = codecs.open(
            'jd_category_utf8.json', 'w', encoding='utf-8')

    def open_spider(self, spider):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db]

    def process_item(self, item, spider):
        self.categoryList.append(dict(item))
        return item

    def close_spider(self, spider):
        category_collection: Collection = self.db[collection_name]
        category_collection.insert_many(self.categoryList)
        self.client.close()

        # 对象转换成dict
        # def obj2dict(self, obj):
        #     if isinstance(obj, JDFirstCategoryItem) or isinstance(obj, JDSecondCategoryItem):
        #         return dict({'name': obj['name'], 'categoryList': obj['categoryList']})
        #     return dict(obj)

        # 文件json存储
        # item = CategoryManager.default_manager(CategoryManager).insert_categories(self.categoryList)
        # self.file.write(json.dumps(self.categoryList,
        #                            default=self.obj2dict,
        #                            indent=1,
        #                            sort_keys=False,
        #                            ensure_ascii=False))
        # self.file.close()
