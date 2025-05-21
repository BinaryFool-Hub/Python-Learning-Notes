import webview  # 导入依赖包


class Api(object):
    """
    创建一个用于数据处理传递的类
    """

    def __init__(self):
        self.users = []  # 存储数据的容器

    def add_user(self, name):
        """
        处理数据板块
        """
        print("用户插入的数据:", name)
        self.users.append(name)
        return self.users


if __name__ == '__main__':
    api = Api()  # 实例化类

    """
    title:GUI程序标题名称
    url:你的web页面HTML位置
    js_api:提供给js调用的api类
    """
    window = webview.create_window(title='用户管理', url='static/web/index.html', js_api=api)

    webview.start(debug=False)  # debug=True会打开一个开发者工具，以便开发者调试，非开发化境建议关闭，默认False
