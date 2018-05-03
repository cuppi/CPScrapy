# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy_splash import SplashRequest


class SNGoodsSpider(scrapy.Spider):
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
                                    'menuIndex': 1
                                },
                                endpoint='execute')

    def jdCategoryParse(self, response):
        pass
