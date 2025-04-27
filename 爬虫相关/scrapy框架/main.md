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

# 编写爬虫项目

## 01 创建项目

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

## 02 进一步初始化设置

1. 在 settings.py 文件中关闭robots协议
2. 在爬虫文件下修改起始网址<start_urls>
3. 注释限制允许的域 allowed_domains = \["example.com"] 这样不会限制爬取的网址
4. 在 parse 方法下面解析数据
5. 在 items.py 文件中定义数据结构
6. 在 pipelines.py 文件中写保存数据的逻辑
7. 在 settings.py 配置文件中打开管道配置

## 03 项目运行

```shell
# 运行的时候一定要先切换终端路径到项目目录
scrapy crawl (爬虫文件名字)

# 无日志输出运行，但是会输出print
scrapy crawl (爬虫文件名字)  --nolog
```

# 扩展

跨域网址 标志: x-requested-with: XMLHttpRequest
