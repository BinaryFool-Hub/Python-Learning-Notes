import scrapy


class Spider3Spider(scrapy.Spider):
    name = "spider_3"

    def start_requests(self):
        yield scrapy.http.Request(
            url='https://example.com',

            # 不会导致中间件的cookies失效，只是添加或更新了
            cookies={'new_value': '111'},

            callback=self.parse
        )

    def parse(self, response):
        pass
