# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDFirstCategoryItem(scrapy.Item):
    name: str = scrapy.Field()
    category_list: list = scrapy.Field()


class JDSecondCategoryItem(scrapy.Item):
    name: str = scrapy.Field()
    category_list: list = scrapy.Field()


class JDThirdCategoryItem(scrapy.Item):
    name: str = scrapy.Field()


class SNThirdCategoryItem(scrapy.Item):
    name: str = scrapy.Field()
    category_href: str = scrapy.Field()
    category_id: str = scrapy.Field()
    is_accurate_category: bool = scrapy.Field()
