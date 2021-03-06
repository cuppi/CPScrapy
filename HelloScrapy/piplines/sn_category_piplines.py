# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from ..spiders.sn_category import SNCategorySpider


class SNCategoryPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri_name: str = mongo_uri
        self.mongo_db_name: str = mongo_db
        self.client: MongoClient = None
        self.db: Database = None

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
        if isinstance(spider, SNCategorySpider):
            category_collection: Collection = self.db['sn_category_collection']
            category_collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
