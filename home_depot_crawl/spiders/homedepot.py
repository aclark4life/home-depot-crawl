# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from home_depot_crawl.items import LightBulb
import xlwt


def output(items):
    """
    Via http://stackoverflow.com/questions/13437727/python-write-to-excel-spreadsheet
    """
    book = xlwt.Workbook()
    sheet = book.add_sheet('1')
    count = 0
    sheet.write(count, 0, 'Light Bulbs')
    count += 1
    for item in items:
        sheet.write(count, 0, item['name'])
        count += 1
    book.save('homedepot.xls')


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
        # Select all the light bulbs in the products div
        bulbs = sel.xpath('//*[@id="products"]/div')
        items = []

        for bulb in bulbs:
            item = LightBulb()
            # Select the description relative to the first div
            item['name'] = ' '.join(bulb.xpath('div//a[@class="item_description"]/text()').re('\w+'))
            items.append(item)

        output(items)
        return items
