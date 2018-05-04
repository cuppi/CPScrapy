# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from ..spiders.jd_category import JDCategorySpider

COLLECTION_NAME = 'jd_category_collection'


class JDCategoryPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri_name: str = mongo_uri
        self.mongo_db_name: str = mongo_db
        self.client: MongoClient = None
        self.db: Database = None
        self.category_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri_name)
        self.db = self.client[self.mongo_db_name]

    def process_item(self, item, spider):
        if isinstance(spider, JDCategorySpider):
            self.category_list.append(dict(item))
        return item

    def close_spider(self, spider):
        if isinstance(spider, JDCategorySpider):
            category_collection: Collection = self.db[COLLECTION_NAME]
            category_collection.insert_many(self.category_list)
        self.client.close()

        # 对象转换成dict
        # def obj2dict(self, obj):
        #     if isinstance(obj, JDFirstCategoryItem) or isinstance(obj, JDSecondCategoryItem):
        #         return dict({'name': obj['name'], 'category_list': obj['category_list']})
        #     return dict(obj)

        # 文件json存储
        # item = CategoryManager.default_manager(CategoryManager).insert_categories(self.category_list)
        # self.file.write(json.dumps(self.category_list,
        #                            default=self.obj2dict,
        #                            indent=1,
        #                            sort_keys=False,
        #                            ensure_ascii=False))
        # self.file.close()
