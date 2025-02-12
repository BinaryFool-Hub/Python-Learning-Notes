# 多态的意思是一个类中传递其他的实例化，然后内部调用方法或属性

class AObj(object):
    def __init__(self, name):
        self.name = name

    def work(self):
        return f'{self.name}正在工作'


class BObj(object):
    def __init__(self, name):
        self.name = name

    def work(self):
        return f'{self.name}正在工作'


class CObj(object):
    def __init__(self, name):
        self.name = name

    def event(self, obj_info):
        print(obj_info.name)
        print(f'{self.name}的属下{obj_info.work()}')


a = AObj('小明')
b = BObj('小红')
c = CObj('领导')

c.event(a)
c.event(b)
