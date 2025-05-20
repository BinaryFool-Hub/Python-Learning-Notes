import scrapy


class Spider1Spider(scrapy.Spider):
    name = "spider_1"

    def start_requests(self):
        """
        这是一次性请求头的添加
        """
        yield scrapy.http.Request(
            url='https://www.baidu.com',
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
            },
            callback=self.parse
        )

    def parse(self, response):
        print("状态码：", response.status)
        pass
