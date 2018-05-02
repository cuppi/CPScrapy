from pymongo import MongoClient
from pymongo import database


class Singleton:
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


class DBManager(Singleton):
    def __init__(self):
        self.client: MongoClient = None
        self.db: database = None
        self.create_manager()

    @staticmethod
    def default_manager(self):
        return self()

    def create_manager(self):
        # client = MongoClient('mongodb://localhost:27017/')
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.jd_scrapy_data
