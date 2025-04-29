import scrapy


class Spider2Spider(scrapy.Spider):
    name = "spider_2"
    allowed_domains = ["a.com"]
    start_urls = ["https://a.com"]

    def parse(self, response):
        pass
