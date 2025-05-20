"""
整体流程总结：
导入爬虫 ➔ 实例化调度器 ➔ 注册爬虫 ➔ 启动运行
"""

from scrapy.crawler import CrawlerProcess  # 爬虫调度器类

from project_3.spiders.spider_1 import Spider1Spider  # 你写好的爬虫类
from project_3.spiders.spider_2 import Spider2Spider  # 你写好的爬虫类

process = CrawlerProcess()
"""
实例化调度类对象
默认会使用 settings.py 配置（也可以自己传入自定义配置）：
    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'ERROR',
        'USER_AGENT': 'my-custom-agent',
    })
"""

process.crawl(Spider1Spider)
process.crawl(Spider2Spider)
"""
注册爬虫，有多个就写多个，但是只能当前项目下的爬虫，它们会顺序一个一个执行
如果你的爬虫有 __init__ 方法需要接收参数，可以这么写：
    process.crawl(MySpider, arg1="xxx", arg2="yyy")
    相当于：
    MySpider(arg1="xxx", arg2="yyy")
"""

process.start()  # 正式启动调度器，开始运行爬虫。会阻塞等待，直到爬虫跑完
