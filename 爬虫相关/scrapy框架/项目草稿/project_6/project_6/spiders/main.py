import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import Project6Item


class MainSpider(RedisSpider):
    name = "main"
    redis_key = "main:start_urls"

    def parse(self, response):
        href_content = response.css("#senfe tr td a[target='_blank']")
        for item in href_content:
            link = item.css("::attr(href)").get()
            city = item.css("::text").get().strip()

            yield scrapy.Request(url=link, meta={"city": city}, callback=self.parse_next_link)

    def parse_next_link(self, response):
        url = response.css("div[track-id='newhouse'] a::attr(href)").get()
        print("next_link", url, response.meta['city'])
        yield scrapy.Request(url=url, meta=response.meta, callback=self.parse_info)

    def parse_info(self, response):
        houses_info = response.css("#newhouse_loupan_list ul li")
        for item in houses_info:
            title = item.css(".clearfix .nlc_details .house_value.clearfix a::text").get().strip()
            style = "".join(item.css(".clearfix .nlc_details .house_type.clearfix *::text").getall())
            address = item.css(".clearfix .nlc_details .relative_message.clearfix .address a::text").get()
            price = "".join(item.css(".clearfix .nlc_details .price_fix *::text").getall())

            yield Project6Item(title=title, style=style, address=address, price=price)
