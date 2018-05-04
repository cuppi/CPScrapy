# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
from pymongo import MongoClient
from pymongo.database import Database

mongo_uri = 'mongodb://localhost:27017/'
mongo_db = 'scrapy_data'


class SNGoodsPipeline(object):
    def __init__(self):
        self.client = None
        self.db: Database = None
        self.category_list = []

    def open_spider(self, spider):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db]

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        self.client.close()
