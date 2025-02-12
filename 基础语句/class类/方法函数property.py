class Test(object):
    def __init__(self, name):
        self.name = name

    # 方法函数
    @property  # 作用: 可以将这个方法通过属性的形式调用  仅限于类中的函数没有参数的时候才可以这样用
    def print_name(self):
        return f'{self.name}正在吃东西'


obj_info = Test('小明')

print(obj_info.print_name)
