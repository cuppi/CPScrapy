from .dbmanager import DBManager
from pymongo.collection import Collection


class CategoryManager(DBManager):
    # @staticmethod
    # def default_manager():
    #     return CategoryManager()

    def insert_categories(self, categories):
        category_collection: Collection = self.db.category_collection
        category_collection.insert_many(categories)

    def find_item(self):
        category_collection: Collection = self.db.category_collection
        return category_collection.find_one({'name': 'test'})