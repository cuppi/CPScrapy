from scrapy import cmdline
from util.dbmanager import DBManager

# item = DBManager.default_manager().insert_item()
# item = DBManager.default_manager().find_item()
# print(item);
cmdline.execute("scrapy crawl example".split())

