import scrapy

from ..items import Spider3Item  # 返回上级导入容器


class Spider2Spider(scrapy.Spider):
    name = "spider_3"
    # allowed_domains = ["a.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for item in response.css(".quote"):
            text = item.css(".text::text").get()
            author = item.css(".author::text").get()
            tags = item.css("a.tag::text").getall()

            """
            因为scrapy是异步框架，所以可以不需要等待全部数据解析完成再返回，解析了一部分就返回一部分
            可以使用scrapy给我们提供的数据容器返回，`items.py`文件中需要自己定义容器字段
            scrapy框架里面所有爬虫文件返回数据都是用yield
            返回的数据会流入到管道文件`pipelines.py`
            """
            yield Spider3Item(text=text, author=author, tags=tags)
