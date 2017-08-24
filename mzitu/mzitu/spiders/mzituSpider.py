# -*- coding: utf-8 -*-
# /usr/bin/env python
import scrapy
from mzitu.items import MzituItem 

class MzituspiderSpider(scrapy.Spider):
    name = 'mzituSpider'
    allowed_domains = ['www.meizu.com']
    start_urls = ['http://www.mzitu.com/99955']

    def parse(self, response):
        body = response.xpath('//div[@class="main-image"]')

        #print body.extract()
        for n in body:
            item = MzituItem()
            item['url'] = n.xpath('.//img/@src')
            item['name'] = n.xpath('.//img/@alt')
            yield item
            SUM = response.xpath('.//div[@class="pagenavi"]/a[last()-1]/span/text()')
            #print SUM.extract()
            for n in (2,SUM):
                newurl = response.url + '/' + str(n)
                print newurl
                yield scrapy.Request(newurl,callback = self.parse)
