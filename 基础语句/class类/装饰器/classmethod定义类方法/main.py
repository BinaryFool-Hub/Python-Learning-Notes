"""
@classmethod 是用来定义类方法的装饰器

第一个参数是 cls（不是 self），代表类本身
可以用来操作类属性、创建类的变种实例等
"""


class ClassEvent(object):
    @classmethod
    def class_method(cls, parameter):
        print(f'这是类方法的参数传递: {parameter}')
        return '这是一个类方法'


obj_info = ClassEvent()

print(obj_info.class_method('数据'))
