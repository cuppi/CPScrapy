# -*- coding: utf-8 -*-
import scrapy
from ..items import HelloscrapyItem

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        item = HelloscrapyItem()
        for text in response.xpath('//div[@class="quote"]/span[1]/text()').extract():
            item['text'] = text
            yield item
