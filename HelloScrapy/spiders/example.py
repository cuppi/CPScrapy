# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import JDFirstCategoryItem
from ..items import JDSecondCategoryItem
from ..items import JDThirdCategoryItem
from scrapy_splash import SplashRequest

lua_script = ''
with open(os.path.join(os.getcwd(), 'HelloScrapy', 'spider.lua'), 'r') as f:
    lua_script += f.read()


class ExampleSpider(scrapy.Spider):
    name = 'example'
    crawlUrl = 'https://so.m.jd.com/webportal/channel/m_category?searchFrom=home'
    start_urls = [
        crawlUrl,
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.jdCategoryParse,
                                args={
                                    'lua_source': lua_script,
                                    'menuIndex': 35
                                },
                                endpoint='execute')
            # endpoint='render.html')

    def jdCategoryParse(self, response):
        if hasattr(response, 'data'):
            carry_data = response.data['carryData']
            current_index = carry_data['currentIndex']
            menu_length = carry_data['menuLength']
            menu_name = carry_data['menuName']
            if current_index + 1 >= menu_length:
                print('爬虫结束')
                return
            print('menu当前索引是 ', current_index)
            first_item = JDFirstCategoryItem(categoryList=[])
            first_item['name'] = menu_name
            second_category_list: list = response.xpath('//div[contains(@class, "jd-category-div")]')
            for secondCategory in second_category_list:
                second_item = JDSecondCategoryItem(categoryList=[])
                second_item['name'] = secondCategory.xpath('h4/text()').extract_first()
                for trirdCategory in secondCategory.xpath('ul/li//span/text()').extract()[:]:
                    trird_item = JDThirdCategoryItem()
                    trird_item['name'] = trirdCategory
                    second_item['categoryList'].append(trird_item)
                first_item['categoryList'].append(second_item)
            yield first_item
            yield SplashRequest(url=response.url,
                                callback=self.jdCategoryParse,
                                args={
                                    'lua_source': lua_script,
                                    'menuIndex': current_index + 1
                                },
                                endpoint='execute')
        else:
            print('没有找到carryData')
