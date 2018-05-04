# -*- coding: utf-8 -*-
import scrapy, re
from ..items import SNThirdCategoryItem
from scrapy_splash import SplashRequest
from util.lua_loader import LuaLoader
lua_script = LuaLoader.load_script('sn_category.lua')


class SNCategorySpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'HelloScrapy.piplines.sn_category_piplines.SNCategoryPipeline': 300,
        }
    }
    name = 'sn_category'
    crawlUrl = 'https://m.suning.com/list/list.html'
    start_urls = [
        crawlUrl,
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.snCategoryParse,
                                args={
                                    # 'lua_source': lua_script,
                                    # 'menuIndex': 30
                                },
                                endpoint='render.html')

    def snCategoryParse(self, response):
        # if hasattr(response, 'data'):
        #     carry_data = response.data['carryData']
        #     current_index = carry_data['currentIndex']
        #     menu_length = carry_data['menuLength']
        #     menu_name = carry_data['menuName']
        #     if current_index + 1 >= menu_length:
        #         print('爬虫结束')
        #         return
        #     print('menu当前索引是 ', current_index)
        #     print(menu_name)
        for secondCategory in response.xpath('//div[contains(@class, "household-recommend")]'):
            for trirdCategory in secondCategory.xpath('ul/li//a')[:]:
                title = trirdCategory.xpath('em/text()').extract_first()
                href = trirdCategory.xpath('@href').extract_first()
                category = SNThirdCategoryItem()
                category['is_accurate_category'] = False
                category['name'] = title
                category['category_href'] = href
                if re.match('.*-0.html$', href):
                    category['is_accurate_category'] = True
                    category['category_id'] = re.findall('/[0-9]+-0.html$', href)[0].split('-')[0][1:]
                yield category


                # first_item = JDFirstCategoryItem(categoryList=[])
                # first_item['name'] = menu_name
                # second_category_list: list = response.xpath('//div[contains(@class, "jd-category-div")]')
                # for secondCategory in second_category_list:
                #     second_item = JDSecondCategoryItem(categoryList=[])
                #     second_item['name'] = secondCategory.xpath('h4/text()').extract_first()
                #     for trirdCategory in secondCategory.xpath('ul/li//span/text()').extract()[:]:
                #         trird_item = JDThirdCategoryItem()
                #         trird_item['name'] = trirdCategory
                #         second_item['categoryList'].append(trird_item)
                #     first_item['categoryList'].append(second_item)
                # yield first_item
                # yield SplashRequest(url=response.url,
                #                     callback=self.snCategoryParse,
                #                     args={
                #                         'lua_source': lua_script,
                #                         'menuIndex': current_index + 1
                #                     },
                #                     endpoint='execute')
                # else:
                #     print('没有找到carryData')
