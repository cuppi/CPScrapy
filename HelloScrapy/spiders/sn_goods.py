# -*- coding: utf-8 -*-
import json
import scrapy
from tool.url_tool import UrlTool

class SNGoodsSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'HelloScrapy.piplines.sn_goods_piplines.SNGoodsPipeline': 300,
        }
    }

    def __init__(self):
        self.page = 1
        self.category = 258004
        scrapy.Spider.__init__(self)

    name = 'sn_goods'

    def start_requests(self):
        params = {
            'channelId': 'MOBILE',
            'ci': self.category,
            'cp': self.page,
            'set': 5
        }
        crawlUrl = UrlTool.url_params_from_dict(params,
                                                baseUrl='https://search.suning.com/emall/mobile/clientSearch.jsonp')
        yield scrapy.Request(url=crawlUrl,
                             method='POST',
                             callback=self.sn_goods_parse)

    def sn_goods_parse(self, response):
        self.page += 1
        data = json.loads(response.text)
        goodsCount: int = data['goodsCount']
        brandSize: int = data['brandSize']
        print(data['goods'])
        # yield dict(data['goods'])

    def parse(self, response):
        pass
