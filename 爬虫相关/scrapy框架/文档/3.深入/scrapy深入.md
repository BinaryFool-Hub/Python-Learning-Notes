## 1、Item数据结构

​		`Item`是保存爬取数据的容器,它的使用方法和字典类似。不过,相比字典,`Item`提供了额外的保护机制,可以避免拼写错误或者定义字段错误。

​		创建`Item`需要继承`scrapy.Item`类,并且定义类型为`scrapy.Field`的字段。在创建项目开始的时候`Item`文件是这样的。

```python
import scrapy

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # 参照下面这个参数定义你的字段
    # name = scrapy.Field()
    pass
```

​		在保存数据的时候可以每次初始化一个字典等格式，但是最方便，最好的保存方式就是使用 Scrapy 自带的 Item 数据结构了。

我们学习了从页面中提取数据的方法，接下来学习如何封装爬取到的数据。应该用怎样的数据结构来维护这些零散的信息字段呢？最容易想到是使用Python字典（dict）。

回顾之前的代码

```python
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')

        for quote in quotes:
            text = quote.css('.text::text').get()
            author = quote.css('.author::text').get()
            tags = quote.css('.tag::text').getall()

            yield {
                'text': text,
                'author': author,
                'tags': tags,
            }
```

在该案例中，我们便使用了Python字典存储一条数据的信息，但字典可能有以下缺点：

（1）无法一目了然地了解数据中包含哪些字段，影响代码可读性。

（2）缺乏对字段名字的检测，容易因程序员的笔误而出错。

（3）不便于携带元数据（传递给其他组件的信息）。

为解决上述问题，在Scrapy中可以使用自定义的Item类封装爬取到的数据。

### 1、1 Item 和 Field 

Scrapy提供了以下两个类，用户可以使用它们自定义数据类（如书籍信息），封装爬取到的数据：

#### 1、1、1 Item 基类

数据结构的基类，在items.py中定义数据结构时，需要继承自该基类。

#### 1、1、2 Field 类

用来描述自定义数据类包含哪些字段（如name、price等）。

自定义一个数据类，只需继承Item，并创建一系列Field对象的类属性即可。

以定义书籍信息 quote 为例，它包含个字段，分别为书的名字text、author和tags，代码如下：

```python
# 特殊的字典结构 可以在scrapy中传递数据
class TutorialItem(scrapy.Item):
    # Field 字段
    # 就是类似于产生一个类似字典格式的数据  拥有字典的一些属性
    # 字段默认为空
    # 我们可以通过实例化 像着键赋值 但是如果没有写这个键 就不能赋值 但是字典可以
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
```

Item支持字典接口，因此 TutorialItem 在使用上和Python字典类似。

对字段进行赋值时，TutorialItem 内部会对字段名进行检测，如果赋值一个没有定义的字段，就会抛出异常（防止因用户粗心而导致错误）

### 1、2 多个item处理

```python
from NcepuSpider.items import ArticleViewsCountItem
from NcepuSpider.items import ArticleBodyItem
from NcepuSpider.items import NcepuNewsSpiderItem


def process_item(self, item, spider):
    # 使用isinstance然后通过if判断方式进行items类别筛选
    # 写入json文件
    if isinstance(item, ArticleViewsCountItem):
        pass
    elif isinstance(item, ArticleBodyItem):
        pass
    elif isinstance(item, NcepuNewsSpiderItem):
        pass
    return item
```

## 2、Item Pipeline

​		当 spider 获取到数据（item）之后，就会将数据发送到 Item Pipeline，Item Pipeline 通过顺序执行的几个组件处理它。

​		在Scrapy中，Item Pipeline是处理数据的组件，一个Item Pipeline就是一个包含特定接口的类，通常只负责一种功能的数据处理，在一个项目中可以同时启用多个Item Pipeline，它们按指定次序级联起来，形成一条数据处理流水线。

Item Pipeline 的典型用途是：

+ 清理HTML数据
+ 验证的数据（检查项目是否包含某些字段）
+ 进行数据的保存

### 2、1 Item Pipeline 使用

​		Scrapy 提供了 `pipeline` 模块来执行保存数据的操作。在创建的 Scrapy 项目中自动创建了一个 `pipeline.py` 文件，同时创建了一个默认的 `Pipeline` 类：

```python
class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
```

在这个类中，有个方法叫 process_item() 方法，每个 Pipeline 都需要调用该方法。

process_item() 方法必须返回一个字典数据。默认有两个参数。如果把 Item 删除了那就不会再调用其他 Pipeline 方法了。

参数：

+ **item** ( Item 对象 dict) 

+ **spider** (Spider 对象) 

既然有了数据，那么就可以保存了：

```python
class Qd03EnglishPipeline:
    def process_item(self, item, spider):
        print('item_info_2', item)
        with open('english.csv', mode='a', encoding='utf-8') as f:
            f.write(item['title'] + ',' + item['info'] + ',' + item['img_url'])
            f.write('\n')
        return item
```

### 2、2 启用 Item Pipeline组件

只是上面定义方法还不行，还要激活该组件，也就是激活管道文件才能保存数据。激活是在配置文件`setteings.py`文件中激活，在配置文件中找到如下变量值取消注释：

```python
ITEM_PIPELINES = {
   'qd_03_english.pipelines.Qd03EnglishPipeline': 300,
}
```

**重点：**

在上图中的字典结构的配置中，键是管道文件所在的路径，值是该管道文件的激活顺序，**数字越小代表越早激活** 。因为有时候会有多个管道文件。

**完整的 item pipeline **

```python
import something

class SomethingPipeline(object):
    def __init__(self):    
        ## 可选实现，做参数初始化等
        ## doing something
        pass
    
    def open_spider(self, spider):
        ## spider (Spider 对象) – 被开启的spider
        ## 可选实现，当spider被开启时，这个方法被调用。
        pass
    
    def process_item(self, item, spider):
        ## item (Item 对象) – 被爬取的item
        ## spider (Spider 对象) – 爬取该item的spider
        ## 这个方法必须实现，每个item pipeline 组件都需要调用该方法，
        ## 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
        return item

    def close_spider(self, spider):
        ## spider (Spider 对象) – 被关闭的spider
        ## 可选实现，当spider被关闭时，这个方法被调用
        pass
```

* 写入JSON文件

以下 pipeline 将所有(从所有'spider'中)爬取到的item，存储到一个独立地items.json 文件，每行包含一个序列化为'JSON'格式的'item'。

```python
class JSONPipeline:
    def __init__(self):
        self.f = open('data.json', mode='w', encoding='utf-8')
        # 收集每一条 item 数据
        self.d_list = []

    def process_item(self, item, spider):
        d = dict(item)
        return item

    def close_spider(self, spider):
        self.f.write(json.dumps(self.d_list, ensure_ascii=False))
        return item
        self.f.close()
```

* 写入CSV文件

  ~~~python
  class CSVPipeline:
      def __init__(self):
          self.f = open('data.csv', mode='a', encoding='utf-8', newline='')
          self.csv_write = csv.DictWriter(self.f, ['title', 'info', 'img_url'])
          self.csv_write.writeheader()
  
      def process_item(self, item, spider):
          d = dict(item)
          self.csv_write.writerow(d)
          return item
  
      def close_spider(self, spider):
          self.f.close()
  ~~~

**注意：一定要修改配置文件**

在写好以后要在配置文件 `settings.py` 中激活，并指定激活顺序。

~~~python
ITEM_PIPELINES = {
   'qd_03_english.pipelines.Qd03EnglishPipeline': 300,
   'qd_03_english.pipelines.CSVPipeline': 299,
   'qd_03_english.pipelines.JSONPipeline': 298,
}
~~~

**注意：一定要修改配置文件**

在写好以后要在配置文件 `settings.py` 中激活，并指定激活顺序。

### 2、4 保存到数据库

#### 2、4、1 保存到Redis数据库

保存到数据库和保存到文件中格式类似的，只不过初始化的时候，将本来是打开文件的操作，转为连接数据库的操作。写入的时候将本来是写入到文件的操作转为写入到数据库中的操作。以`Redis`数据库为例：

```python
# 这个是保存到redis
class RedisPipeline(object):

    def __init__(self):
        ## 初始化链接reids
        self.redis_cli = redis.StrictRedis(
            host='127.0.0.1',
            port=6379,
            db=1,
        )

    def process_item(self, item, spider):
        ## 保存到redis
        self.redis_cli.lpush('quotes', json.dumps(dict(item)))
        return item

    def close_spider(self, spider):
        self.redis_cli.close()
```

#### 2、4、2 保存到MySQL数据库

```python
# 这个是保存到mysql
class MySQLPipeline(object):
    """
    create database quotes charset=utf8;
    use quotes;
    create table quotes (txt text, author char(20), tags char(200));
    """

    def __init__(self):
        self.connect = pymysql.connect(
            host='192.168.159.128',
            port=3306,
            db='quotes',  # 数据库名
            user='windows',
            passwd='123456',
            charset='utf8',
            use_unicode=True
        )
        # 创建操作数据的游标
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 保存到mysql
        # 执行sql语句
        self.cursor.execute(
            'insert into quotes (txt, author, tags) value(%s, %s, %s)' % (item['text'], item['author'], item['tags'])
        )
        # 提交数据执行数据
        self.connect.commit()
        return item

    # 关闭链接
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

```

#### 2、4、3 将数据存入MongoDB 

有时，我们想把爬取到的数据存入某种数据库中，可以实现Item Pipeline完成此类任务。下面实现一个能将数据存入MongoDB数据库的Item Pipeline，代码如下：

对上述代码解释如下。

●　在类属性中定义两个常量：

DB\_URI　数据库的URI地址。

DB_NAME　数据库的名字。

```python
from scrapy.item import Item
import pymongo


class MongoDBPipeline(object):


    DB_URI = 'mongodb://localhost:27017/'
    DB_NAME = 'scrapy_data'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URI)
        self.db = self.client[self.DB_NAME]
    
    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item

    def close_spider(self, spider):
    	self.client.close()
```

### 2、5 文件下载

下载文件也是实际应用中很常见的一种需求，例如使用爬虫爬取网站中的图片、视频、WORD文档、PDF文件、压缩包等。本章来学习在Scrapy中如何下载文件和图片。

scrapy专门封装了一个下载图片的  `ImagesPipeline`， 使用 `ImagesPipeline` for图像文件的优点是，您可以配置一些额外的功能，例如生成缩略图和根据图像大小过滤图像。 

**FilesPipeline和ImagesPipeline **

Scrapy框架内部提供了两个Item Pipeline，专门用于下载文件和图片：

●　FilesPipeline

●　ImagesPipeline

我们可以将这两个Item Pipeline看作特殊的下载器，用户使用时只需要通过item的一个特殊字段将要下载文件或图片的url传递给它们，它们会自动将文件或图片下载到本地，并将下载结果信息存入item的另一个特殊字段，以便用户在导出文件中查阅。下面详细介绍如何使用它们。

#### 2、5、1 ImagesPipeline使用说明 

目标网址：https://www.vmgirls.com/12985.html

有时候可能会采集图片资源，Scrapy帮我们实现了图片管道文件，很方便保存图片：

```python
class LiangliSpider(scrapy.Spider):
    name = 'liangli'
    allowed_domains = ['hexuexiao.cn']
    start_urls = ['https://www.hexuexiao.cn/a/124672.html']

    def parse(self, response):
        # print(response.text)
        title = response.css('h1::text').get()
        title = re.findall('[\u4e00-\u9fa5]+', title)[0]
        urls = response.css('a.btn-default::attr(href)').get()  # 提取当前页面图片的链接地址
        item = QdLiangliItem(title=title, urls=urls)
        yield item
```

重点：

- `get_media_requests()`是用来发送请求的，需要传入图片的网址。
- `file_path()`是用来指定保存的文件的名字。
- 除了编写图片管道文件，还要在配置环境中激活，以及指定图片的存储位置。

```python
class DownloadPicturePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item, QdLiangliItem_2):
            """把图片的下载地址构建成一个requests请求"""
            for url in item['urls']:
                # 构建一个请求之前, 如果有 file_path 函数, 会被这个函数预先处理
                yield scrapy.Request(url, meta={'title': item['title']})

    def file_path(self, request, response=None, info=None, *, item=None):
        """
        指定文件保存的路径, 重命名，若不重写这函数，图片名为哈希
        :param request:
        :return: 文件路径
        """
        # 获取item里面图片系列的名字
        dir_name = request.meta.get('title')
        # 通过split分割, 取出图片的名字
        file_name = request.url.split('/')[-1]
        # return 返回文件路径
        return os.path.join(dir_name, file_name)  # os.path.join 构造路径位置
```

#### 2、5、2 FilesPipeline使用说明 

使用FilesPipeline下载页面中所有PDF文件，可按以下步骤进行：

在配置文件settings.py中启用FilesPipeline，通常将其置于其他Item Pipeline之前：

```
ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
```

在配置文件settings.py中，使用FILES\_STORE指定文件下载目录，如：

```
FILES_STORE = '/home/liushuo/Download/scrapy'
```

在Spider解析一个包含文件下载链接的页面时，将所有需要下载文件的url地址收集到一个列表，赋给item的file\_urls字段（item\['file\_urls'\]）。FilesPipeline在处理每一项item时，会读取item\['file\_urls'\]，对其中每一个url进行下载，Spider示例代码如下：

```python
     class DownloadBookSpider(scrapy.Spider):
        ...

        def parse(response):
            item = {}
            # 下载列表
            item['file_urls'] = []
            for url in response.xpath('//a/@href').extract():
                download_url = response.urljoin(url)
                # 将url 填入下载列表
                item['file_urls'].append(download_url)
     			yield item
```

当FilesPipeline下载完item\['file\_urls'\]中的所有文件后，会将各文件的下载结果信息收集到另一个列表，赋给item的files字段（item\['files'\]）。下载结果信息包括以下内容：

●　Path文件下载到本地的路径（相对于FILES\_STORE的相对路径）。

●　Checksum文件的校验和。

●　文件的url地址。