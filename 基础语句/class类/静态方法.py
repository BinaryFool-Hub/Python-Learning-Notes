class ClassEvent(object):

    def __init__(self):
        pass

    # 静态方法的定义
    @staticmethod
    def class_method(parameter):
        print(f'这是静态方法的参数传递: {parameter}')
        return '这是一个静态方法'


obj_info = ClassEvent()

print(obj_info.class_method('数据'))
