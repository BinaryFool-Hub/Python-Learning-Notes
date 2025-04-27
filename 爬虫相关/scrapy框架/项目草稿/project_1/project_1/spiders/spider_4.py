import scrapy


class Spider4Spider(scrapy.Spider):
    name = "spider_4"

    def start_requests(self):
        """
        scrapy.FormRequest() == scrapy.http.FormRequest()
        Scrapy 官方只给常用的几个请求类做了简写导入，所以这两个没区别

        scrapy.FormRequest() 可以发送post请求，需要注意的是此对象需要对应 Form Data 提交的请求参数才可以使用
        使用yield来返回数据是scrapy的遵循规则（固定的）
        如果你是有规律的或有需求的可以使用for来进行循环请求，使用yield返回scrapy请求对象即可
        """
        yield scrapy.FormRequest(
            url='https://example.com',

            # 请求的form data 数据
            formdata={
                'name': '小明',
                'age': 19
            },

            # 回调函数，本次请求你需要使用哪个函数来处理数据
            callback=self.parse
        )

    def parse(self, response):
        print("拿到了数据：", response.text)
