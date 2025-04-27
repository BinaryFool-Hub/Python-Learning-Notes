import scrapy


class Spider1Spider(scrapy.Spider):
    # 爬虫的名字,通过`scrapy genspider spider_1 a.com`时创建, 后期启动爬虫项目的时候需要指定爬虫的名字
    name = "spider_1"

    # 限制只采集哪个域名下的数据，在实际使用的是后不需要限制，直接注释`allowed_domains`即可
    allowed_domains = ["baidu.com"]

    # 数据的起始网址,只要是在这个列表里面的网址会默认发送请求(如果地址是有规律的, 那么可以用列表推导是构建)
    # 默认是根据`scrapy genspider spider_1 a.com`指定域名自动生成的, 一般是错误的, 需要修改成正确的地址
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        """
        运行爬虫时会使用get请求start_urls里面的网址并且返回给该函数
        response = request<请求体> + response<响应体> + parsel<css, xpath, re>
        数据处理就在该函数中
        这函数名字一定不能改
        """
        pass
