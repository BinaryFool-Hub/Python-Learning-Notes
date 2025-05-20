import scrapy

from ..items import CustomizeItem, CustomizeItem1


class Spider1Spider(scrapy.Spider):
    name = "spider_1"
    allowed_domains = ["a.com"]
    start_urls = ["https://a.com"]


    def parse(self, response):
        """
        这里编写数据提取操作,然后赋值给参数
        """
        name = "小明"
        age = 19
        note = "不吃香菜"

        """先返回给一个容器，因为是异步操作，同一个数据先到这里返回"""
        yield CustomizeItem(
            name=name,
            age=age
        )

        """返回给第二个容器, 因为是异步操作，同一个数据先到上面返回，再经过这里返回"""
        yield CustomizeItem1(
            name=name,
            age=age,
            note=note
        )
