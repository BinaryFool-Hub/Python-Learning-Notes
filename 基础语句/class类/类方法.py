class ClassEvent(object):

    def __init__(self):
        pass

    # 类方法的定义
    @classmethod
    def class_method(cls, parameter):
        print(f'这是类方法的参数传递: {parameter}')
        return '这是一个类方法'


obj_info = ClassEvent()

print(obj_info.class_method('数据'))
