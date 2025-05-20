import scrapy


class Spider6Spider(scrapy.Spider):
    name = "spider_7"

    def start_requests(self):
        """
        meta 是用来在请求之间传递数据的。
        简单说就是：
            你可以通过 meta 把一些临时信息，从一个请求传给下一个请求。
        """
        yield scrapy.Request(
            # 只能拼接查询参数，不能像requests模块一样构建
            url='https://example.com?name=小明',
            callback=self.parse,

            # 传递给下一个请求，使用meta来传递
            meta={'name': '小明', 'age': 19}
        )

    def parse(self, response):
        print("meta传递的数据：", response.meta['name'], response.meta['age'])
        print("拿到了数据：", response.text)
