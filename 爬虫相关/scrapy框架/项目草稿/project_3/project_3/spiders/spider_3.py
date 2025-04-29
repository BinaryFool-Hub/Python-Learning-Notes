import scrapy


class Spider3Spider(scrapy.Spider):
    name = "spider_3"

    def start_requests(self):
        yield scrapy.http.Request(
            url='https://example.com',
            dont_filter=True  # True不去重，默认是False去重，并且不记录其指纹。下一个一样的请求体会请求后再记录指纹
        )

        # 因为没有写dont_filter=True，所以这个会被记录指纹并且请求，直到下一个一样的请求体才不会执行请求
        yield scrapy.http.Request(
            url='https://example.com'
        )

    def parse(self, response):
        pass
