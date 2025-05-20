# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Project1Pipeline:
    def process_item(self, item, spider):
        """
        流入的数据会用item接收，字典形式，需要保存数据提取就使用字典的方式提取数据

        return item 不能注释或者删除，因为Scrapy 的 pipeline 是一个链式处理机制，
        如果你在某个 process_item 方法里不 return item，这个 item 就不会继续传给后面的 pipeline 或内置组件了。
        如果漏了 return item，后续的 pipeline 根本拿不到数据
        """
        return item
