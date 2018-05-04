from pymongo import MongoClient
from pymongo.database import Database


class DefaultPipeline(object):
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
        return item

    def close_spider(self, spider):
        self.client.close()
