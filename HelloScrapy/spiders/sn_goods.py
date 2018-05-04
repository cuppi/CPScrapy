# -*- coding: utf-8 -*-
import json
import scrapy
import time
from tool.url_tool import UrlTool
from ..items.sn_goods_item import SNGoodsItem

SCRAPY_PAGE = 150


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
        yield scrapy.Request(url=self.url_from_page(self.page),
                             method='POST',
                             callback=self.sn_goods_parse)

    def sn_goods_parse(self, response):
        self.page += 1
        data = json.loads(response.text)
        # goodsCount: int = data['goodsCount']
        # brandSize: int = data['brandSize']
        goodsList: list = data['goods']
        for goods in goodsList:
            yield SNGoodsItem(goods)
        time.sleep(0.5)
        if self.page <= SCRAPY_PAGE:
            yield scrapy.Request(url=self.url_from_page(self.page),
                                 method='POST',
                                 callback=self.sn_goods_parse)

    def url_from_page(self, page):
        params = {
            'channelId': 'MOBILE',
            'ci': self.category,
            'cp': page,
            # 这个不填只能拉倒50页
            'ct': -1,
            'set': 5,
            # 'cityId': '021',
            # 'cn': 7045710260,
            # 'code': '9e19abeaef2288026720332c9e4d16c4',
            # 'istongma': 1,
            # 'iv': -1,
            # 'nonfirst': 1,
            # 'operate': 0,
            # 'ps': 10,
            # 'sesab': 'ABBAA',
            # 'sg': 1,
            # 'st': 0,
            # 'v': 1.21
        }
        return UrlTool.url_params_from_dict(params,
                                            baseUrl='https://search.suning.com/emall/mobile/clientSearch.jsonp')

    def parse(self, response):
        pass
