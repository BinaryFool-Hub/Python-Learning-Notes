import scrapy


class Spider6Spider(scrapy.Spider):
    name = "spider_6"

    def start_requests(self):
        """
        scrapy.Request() == scrapy.http.Request()
        Scrapy 官方只给常用的几个请求类做了简写导入，所以这两个没区别

        scrapy.Request() 可以发送get请求
        使用yield来返回数据是scrapy的遵循规则（固定的）
        如果你是有规律的或有需求的可以使用for来进行循环请求，使用yield返回scrapy请求对象即可
        """
        # 查询的参数scrapy不支持分开构建，只能写在url里面
        yield scrapy.Request(
            url='https://example.com?&name=小明',

            # 回调函数，本次请求你需要使用哪个函数来处理数据
            callback=self.parse
        )

    def parse(self, response):
        print("拿到了数据：", response.text)
