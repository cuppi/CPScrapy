# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import HelloscrapyItem
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
                                callback=self.parse,
                                args={
                                    'lua_source': lua_script,
                                    'menuIndex': 1
                                },
                                endpoint='execute')
            # endpoint='render.html')

    def parse(self, response):
        if hasattr(response, 'data'):
            carry_data = response.data['carryData']
            currentIndex = carry_data['currentIndex']
            menuLength = carry_data['menuLength']
            if currentIndex + 1 >= menuLength:
                print('爬虫结束')
                yield
            print('menu长度是 ', currentIndex)
            print(response.xpath('//div[contains(@class, "jd-category-div")]/h4/text()').extract())
            yield SplashRequest(url=self.crawlUrl,
                                callback=self.parse,
                                args={
                                    'lua_source': lua_script,
                                    'menuIndex': currentIndex + 1
                                },
                                endpoint='execute')
        else:
            print('没有找到carryData')
            # item = HelloscrapyItem()
            # for text in response.xpath('//div[@class="quote"]/span[1]/text()').extract():
            #     item['text'] = text
            #     yield item

    def jdParse(self, response):
        print('test')
