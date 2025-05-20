"""
规则爬虫（CrawlSpider）默认不支持 POST 请求，因为它是通过解析页面中的链接（<a href="...">）来构造 GET 请求 自动跟进的。
只是使用正则规则来匹配网址和请求数据，处理数据和数据保存和普通的scrapy没有区别

crawlspider注意事项
     1. 是从一个页面提取链接, 此页面的数据是解析不到的;    如果需要解析此页面数据, 就不能使用crawlspider
     2. rules存放抓取规则, 是一个元组对象, 可以写多个限制条件;, 满足其中一个规则的链接就会被提取到, 这里是逻辑 或  or
     3. LinkExtractor 是详细的提取规则, 里面可以写多个限制条件, 所有的限制条件都满足的链接才会被提取到, 这里是逻辑 与 and
     4. crawlspider 一般用于在子级页面中, 所有页面结构一样的情况下使用; 如果页面结构不一样建议使用普通的爬虫模板scrapy.Spider去写
"""

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Spider1Spider(CrawlSpider):
    name = "spider_1"
    allowed_domains = ["example.com"]  # 根据情况是否只能当前域名下的数据，不是则注释即可
    start_urls = ["https://example.com"]

    """
    符合规则的网址都会默认发送请求，规则是通过正则进行匹配的，然后请求的数据交给parse_item函数处理
    - follow=True 允许进行下一级页面跟进，不会只采集当前页面的数据
    - allow 里面值填写网址的正则表达式，匹配到满足条件的网址才会进行发送
    """
    """
    allow匹配的url拼接：
        相对路径如 news/123 会被正确拼接成 https://example.com/page/news/123；
        如果是 /news/123（以 / 开头），会拼接为 https://example.com/news/123（从根目录开始）；
    """
    rules = (
        Rule(LinkExtractor(
            allow=r"/index/.*?.html",  # 正则表达式匹配满足条件的网址。匹配的是 URL 路径字符串，不含域名。
            restrict_css=(".table", ".link")  # 限制提取的范围使用css限制，里面写元组，一层一层往下
        ), callback="parse_item", follow=True),

        # 写了多个规则会依次执行，如果规则匹配的连接相同也没关系，内部会自动去重
        Rule(LinkExtractor(
            allow=r"/blog/.*?.html",
            restrict_css=(".header", ".link")
        ), callback="parse_item_blog",  # 可以尝试换一个函数处理不同的规则
            follow=False),  # 不继续跟进了，根据需要写
    )

    def parse_item(self, response):
        """解析数据和普通的爬虫一样"""
        item = {}
        # item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_item_blog(self, response):
        """解析数据和普通的爬虫一样"""
        pass
