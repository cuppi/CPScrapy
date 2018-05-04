# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from ..spiders.sn_goods import SNGoodsSpider

COLLECTION_NAME = 'sn_goods_collection'


class SNGoodsPipeline(object):
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
        if isinstance(spider, SNGoodsSpider):
            goods_collection: Collection = self.db[COLLECTION_NAME]
            goods_collection.update_one({'catentry_id': item['catentry_id']},
                                        {"$set": dict(item),
                                         "$currentDate": {"last_updated": True}},
                                        upsert=True)
        return item

    def close_spider(self, spider):
        self.client.close()
