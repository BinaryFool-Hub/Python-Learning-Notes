# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline  # 专门用于保存图片的类
from scrapy.pipelines.files import FilesPipeline  # 专门用于保存二进制文件的类


class SaveImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        """
        固定的格式，不能改变
        往下编写你的请求即可，会自动处理你请求下载的图片
        """
        for url in item['urls']:  # 如果你传入的是一个列表可以这样编写，如果是一个就单独写就行
            yield scrapy.Request(  # 和在爬虫文件`start_requests`函数中请求方法一样写的，post就post，但是一般图片都是get
                # 参数如果有headers和cookies等也可以传入
                url=url,
                meta={'title': item['title']}  # 用于传入到下一个函数使用
            )

    def file_path(self, request, response=None, info=None, *, item=None):
        """
        指定文件保存的路径, 重命名，若不重写这函数，图片名为哈希
        :return: 文件路径
        """
        dir_name = request.meta.get('title')  # `get_media_requests`函数使用请求体中的meta参数传递下来的

        return dir_name  # return返回的结果就是 目录 + 文件名


class CustomizePipeline(object):
    def __init__(self):
        """这是类的构造函数，负责对象实例的初始化，通常只调用一次。"""
        """
        该函数和open_spider效果类似，但是人家框架有就推荐使用人家框架的，一般不使用这个，注释忽略即可
        """

    def open_spider(self, spider):
        """不能更改的方法名和参数"""
        """
        是在爬虫启动时调用的，专门用于爬虫级别的初始化。
        框架项目的初始化方法，每次项目启动的时候只会执行一次，一般用于打开文件或数据库连接
        """

    def process_item(self, item, spider):
        """不能更改的方法名和参数"""
        """框架的数据流处理方法，每次数据一从item流入就会调用该方法，用于数据处理"""
        """
        流入的数据会用item接收，字典形式，需要保存数据提取就使用字典的方式提取数据

        return item 不能注释或者删除，因为Scrapy 的 pipeline 是一个链式处理机制，
        如果你在某个 process_item 方法里不 return item，这个 item 就不会继续传给后面的 pipeline 或内置组件了。
        如果漏了 return item，后续的 pipeline 根本拿不到数据
        """

        return item

    def close_spider(self, spider):
        """不能更改的方法名和参数"""
        """框架项目的结束调用方法，在整个项目结束前会调用该方法函数，和open_spider函数配套"""


from .items import CustomizeItem, CustomizeItem1  # 需要导入类用于判断是哪个类类型


class TypeJudge(object):
    def process_item(self, item, spider):
        """
        使用isinstance()函数来判断是不是正确的类型
        -- 参数一，数据
        -- 参数二，数据类型（基本数据类型，也可以是类的类型）
        """

        print("传递过来的类型：", type(item))

        if isinstance(item, CustomizeItem):
            print("需要执行的代码")
        elif isinstance(item, CustomizeItem1):
            print("又需要执行的代码")
        else:
            print("都不是，则可以不进行或还要进行其他操作")
            # 如果都不是想要不继续处理则需要记得在这块写  return item

        return item


class SaveFilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        """
        固定的格式，不能改变
        往下编写你的请求即可，会自动处理你请求下载的图片
        """
        for url in item["urls"]:  # 如果你传入的是一个列表可以这样编写，如果是一个就单独写就行
            yield scrapy.Request(  # 和在爬虫文件`start_requests`函数中请求方法一样写的
                # 参数如果有headers和cookies等也可以传入
                url=url,
                meta={'title': item['title']}  # 用于传入到下一个函数使用
            )

    def file_path(self, request, response=None, info=None, *, item=None):
        """
        自定义保存路径：目录+文件名
        """
        dir_name = request.meta.get('title')

        return dir_name  # 返回完整保存路径
