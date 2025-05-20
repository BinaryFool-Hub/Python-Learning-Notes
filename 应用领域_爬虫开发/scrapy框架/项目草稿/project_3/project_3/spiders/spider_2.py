import scrapy
from scrapy.http import HtmlResponse


class Spider2Spider(scrapy.Spider):
    name = "spider_2"

    allowed_domains = ["https://example.com"]

    # start_urls = ["https://example.com"]

    def parse(self, response: HtmlResponse):
        print(response)
        pass
