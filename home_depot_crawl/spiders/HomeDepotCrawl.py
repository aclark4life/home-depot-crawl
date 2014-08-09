# -*- coding: utf-8 -*-
import scrapy


class HomedepotcrawlSpider(scrapy.Spider):
    name = "HomeDepotCrawl"
    allowed_domains = ["homedepot.com"]
    start_urls = (
        'http://www.homedepot.com/',
    )

    def parse(self, response):
        pass
