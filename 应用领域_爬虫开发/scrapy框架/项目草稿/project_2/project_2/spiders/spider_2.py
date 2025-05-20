import scrapy


class Spider1Spider(scrapy.Spider):
    name = "spider_2"

    def start_requests(self):
        """
        这是中间件请求头的添加，每个请求都过使用中间件的请求头
        """
        yield scrapy.http.Request(
            url='https://www.baidu.com',
            callback=self.parse
        )

    def parse(self, response):
        print("状态码：", response.status)
        pass
