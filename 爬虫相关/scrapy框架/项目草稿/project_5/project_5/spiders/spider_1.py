import scrapy
from scrapy_redis.spiders import RedisSpider

from ..items import Project5Item


class Spider1Spider(RedisSpider):
    name = "spider_1"

    redis_key = 'spider_1:start_urls'

    def parse(self, response):
        links = response.css('.quote > span > a::attr(href)').getall()

        for link in links:
            yield scrapy.Request(url='http://quotes.toscrape.com' + link, callback=self.parse1)

    def parse1(self, response):
        born_date = response.css('.author-born-date::text').get()
        born_location = response.css('.author-born-location::text').get()

        item = Project5Item(born_location=born_location, born_date=born_date)
        yield item
