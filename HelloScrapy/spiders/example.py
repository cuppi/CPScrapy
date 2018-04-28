# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import JDCategoryItem
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
                                    'menuIndex': 33
                                },
                                endpoint='execute')
            # endpoint='render.html')

    def jdCategoryParse(self, response):
        if hasattr(response, 'data'):
            carry_data = response.data['carryData']
            currentIndex = carry_data['currentIndex']
            menuLength = carry_data['menuLength']
            parentName = carry_data['parentName']
            if currentIndex + 1 >= menuLength:
                print('爬虫结束')
                return
            print('menu当前索引是 ', currentIndex)
            secondCategoryList = response.xpath('//div[contains(@class, "jd-category-div")]')
            for secondCategory in secondCategoryList:
                secondCategoryTitle = secondCategory.xpath('h4/text()').extract()
                trirdCategoryList = secondCategory.xpath('ul/li//span/text()').extract()

            # secondCategoryTitleList = secondCategoryList.extract()
            # for category in secondCategoryTitleList:
            #     item = JDCategoryItem()
            #     item['name'] = category
            #     item['parentName'] = parentName
            #     yield item
            yield SplashRequest(url=response.url,
                                callback=self.jdCategoryParse,
                                args={
                                    'lua_source': lua_script,
                                    'menuIndex': currentIndex + 1
                                },
                                endpoint='execute')
        else:
            print('没有找到carryData')
