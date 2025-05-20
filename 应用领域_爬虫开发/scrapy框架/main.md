# 介绍

Scrapy 是一个用于 Python 的开源网络爬虫框架，专为高效抓取网页和提取结构化数据而设计。它广泛应用于数据挖掘、监测和自动化测试等领域。

**主要特点**

1. 高效性：基于异步处理，能快速抓取大量数据。
2. 可扩展性：支持自定义中间件、管道和扩展，适应不同需求。
3. 内置功能：自动处理请求、响应、数据提取和存储。
4. 支持多种数据格式：可导出 JSON、CSV、XML 等格式。
5. 强大的选择器：支持 XPath 和 CSS 选择器，便于数据提取。

**核心组件**

1. Spider：定义抓取逻辑和数据提取规则。
2. Item：存储抓取数据的容器。
3. Pipeline：处理抓取的数据，如清洗、验证和存储。
4. Downloader：负责下载网页内容。
5. Scheduler：管理请求队列，决定抓取顺序。

# 官方文档

scrapy官网： https://scrapy.org/

scrapy中文文档：https://www.osgeo.cn/scrapy/intro/overview.html

# 环境搭建（不指定版本不兼容）

```shell
# scrapy框架
pip install scrapy==2.9.0

# scrapy的依赖
pip install Twisted==22.10.0
```

# 创建运行爬虫项目

## 创建项目

1. 创建一个爬虫项目
   ```shell
   scrapy startproject +(项目名字<独一无二>)
   ```
2. cd 切换到爬虫项目目录
   ```shell
   cd 项目名称路径
   ```
3. 创建爬虫文件
    - 域名限制可以随便填写(a.com)，在实际开发过程中不会用到域名限制
   ```shell
      scrapy genspider (+爬虫文件的名字<独一无二的>) (+域名限制)
   ```

## 项目运行

### 使用终端

```shell
# 运行的时候一定要先切换终端路径到项目目录
scrapy crawl (爬虫文件名字)

# 无日志输出运行，但是会输出print
scrapy crawl (爬虫文件名字)  --nolog
```

### 脚本内运行（比如需要嵌入到 Python 脚本/接口中）

- 适合需要在Python脚本里批量跑爬虫或和别的逻辑结合的场景
- 不需要命令行，直接 python your_script.py 执行

```python
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
```

- CrawlerProcess:爬虫调度器类,这个类可以在普通 Python 脚本中启动、管理 Scrapy 爬虫,可以代替命令行，代码内部直接跑爬虫
- process.crawl：注册爬虫，只能注册当前项目下的爬虫类，因为项目会依赖settings.py，scrapy.cfg等文件，如果需要传参直接在后面跟着即可

# 扩展

跨域网址 标志: x-requested-with: XMLHttpRequest
