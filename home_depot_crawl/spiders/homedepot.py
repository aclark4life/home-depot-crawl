# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from home_depot_crawl.items import LightBulb


class HomedepotSpider(Spider):
    name = "homedepot"
    allowed_domains = ["homedepot.com"]
    start_urls = (
        'http://www.homedepot.com/b/Electrical-Light-Bulbs-CFL-Light-Bulbs/N-5yc1vZbmat',
    )

    def parse(self, response):
        """
        """
        sel = Selector(response)
        bulbs = sel.xpath('//div[@id="products"]/div')
        items = []

        for bulb in bulbs:
            item = LightBulb()
            item['name'] = bulb.xpath('a/text()').extract()
            items.append(item)

        return items
