# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Project5Item(scrapy.Item):
    # define the fields for your item here like:
    born_location = scrapy.Field()
    born_date = scrapy.Field()
