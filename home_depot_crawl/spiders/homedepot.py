# -*- coding: utf-8 -*-
import scrapy


class HomedepotSpider(scrapy.Spider):
    name = "homedepot"
    allowed_domains = ["homedepot.com"]
    start_urls = (
        'http://www.homedepot.com/',
    )

    def parse(self, response):
        pass
