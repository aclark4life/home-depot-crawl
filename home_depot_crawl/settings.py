# -*- coding: utf-8 -*-

# Scrapy settings for home_depot_crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'home_depot_crawl'

SPIDER_MODULES = ['home_depot_crawl.spiders']
NEWSPIDER_MODULE = 'home_depot_crawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'home_depot_crawl (+http://www.yourdomain.com)'
