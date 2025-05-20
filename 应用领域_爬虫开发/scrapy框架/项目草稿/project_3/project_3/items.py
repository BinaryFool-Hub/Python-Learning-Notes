# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CustomizeItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()


class CustomizeItem1(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    note = scrapy.Field()
