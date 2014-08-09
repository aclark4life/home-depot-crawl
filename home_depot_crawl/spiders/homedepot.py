# -*- coding: utf-8 -*-
import scrapy


class HomedepotSpider(scrapy.Spider):
    name = "homedepot"
    allowed_domains = ["homedepot.com"]
    start_urls = (
        'http://www.homedepot.com/b/Electrical-Light-Bulbs-CFL-Light-Bulbs/N-5yc1vZbmat',
    )

    def parse(self, response):
        pass
