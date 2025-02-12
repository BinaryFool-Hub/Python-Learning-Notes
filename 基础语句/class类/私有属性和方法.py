# 私有是外部不可直接调用，只有class内部方法可调用，都以 __ 开头才是私有属性

class Test(object):
    def __init__(self, name):
        self.__name = name  # name 是私有属性

    def __self_event(self):
        print('这是一个私有方法的内部调用值', self.__name, sep='')

    def call_event(self):
        self.__self_event()

        return '这是一个公用方法调用的值'


obg_tsts = Test(name='小明')

# 报错
# obg_tsts.__self_event()

obg_tsts.call_event()

"""
暴力破解私有方法调用
_ 表示class，__ 表示访问里面的属性和方法，函数则加括号，否则去除
不推荐使用，这是暴力破解的方法，外部不能知道函数里面的实际代码，只有在知道属性或函数名称才可使用
"""

# 访问属性
print(obg_tsts._Test__name)
# 访问函数
print(obg_tsts._Test__self_event())
