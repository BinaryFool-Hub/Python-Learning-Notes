"""
@property 装饰器的作用是：把方法变成“像属性一样访问”，让你可以用点号访问，而不是调用函数。
"""


class Test(object):
    def __init__(self, name):
        self.name = name

    @property  # 作用: 可以将这个方法通过属性的形式调用  仅限于类中的函数没有参数的时候才可以这样用
    def print_name(self):
        return f'{self.name}正在吃东西'


obj_info = Test('小明')

print(obj_info.print_name)  # 不带小括号，像属性一样访问
