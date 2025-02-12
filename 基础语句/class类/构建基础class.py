class Method(object):  # 类名大写开头，继承 object 父级（可写可不写）
    def __init__(self, name):
        self.name = name

    def show_name(self, info):  # 类里面的函数
        print(f'自定义传入的参数{info}')
        self.class_function()  # 调用本身或继承的函数用 self

    def class_function(self):
        print(self.name)


class_obj = Method(name='小明')  # 实例化

class_obj.show_name(info='数据')  # 调用里面的函数
print(class_obj.name)  # 调用里面的参数
