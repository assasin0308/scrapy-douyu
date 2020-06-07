# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['capi.douyucdn.cn']
    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        data = json.loads(response.text)["data"]
        for each in data:
            item = DouyuItem()
            item['nickname'] = each['nickname']
            item['image_link'] = each['vertical_src']
            item['room_name'] = each['room_name']

            yield item

        self.offset += 20
        scrapy.Request(self.url + str(self.offset),callback=self.parse)

