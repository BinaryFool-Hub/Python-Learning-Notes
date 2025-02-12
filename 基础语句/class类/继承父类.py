# 继承的同时还需要传递父类的参数
# 继承遇到同名函数都优先继承前面的，但属性在本身或者第一个继承中找不到则报错
# 继承传递的参数第一个父级的参数是必须要的
# 继承可自定义属性和方法，它的含义是继承父级所有的方法和属性，所以可以自己自定义属性和方法
# super() 只能按照 MRO 顺序调用一个父类的 __init__ 方法， 因此其他父类还需要则可以使用实例化 __init__ 或者定义新的属性
# super 用于类的单继承关系
# 多继承 在子类里面去调用其他父类的方法和属性  是应该使用类对象方法去调用

class AObj(object):
    def __init__(self, name, info):
        self.name = name
        self.info = info

    def event(self):
        print(f'这是父类的方法输出：{self.name}, {self.info}')


class CObj(object):
    def __init__(self, name, info, other):
        self.name = name
        self.info = info
        self.other = other

    def event(self):
        print(f'这是C类的其他参数值：{self.other}')
        print(f'这是C父类的方法输出：{self.name}, {self.info}')

    def c_event(self):
        print(f'C类的方法{self.other}')


class BObj(AObj, CObj):
    def __init__(self, name, info, self_info_parm, other):
        super().__init__(name, info)  # 继承第一个父类的参数
        self.other = other  # 因为super只能继承第一个类的参数，所以可以在self中定义新的参数

        # 多参数的初始化
        # AObj.__init__(self, name, info)  # 调用AObj的初始化
        # CObj.__init__(self, name, info, other)  # 调用CObj的初始化

        self.self_info_parm = self_info_parm  # 自定义当前类属性值

    def event(self):  # 同名是重写父级函数方法
        print('这是继承父类的同名函数', end='')
        super().event()  # 继承父类的函数，下面是重写，也可以不继承

        print(f'这是继承类的输出: {self.name}, {self.info}')
        print(f'这是继承类自己的属性：{self.self_info_parm}')

    def same_name_method(self):
        # 调用多参数
        print('调用多参数', end='')
        self.c_event()

        # 调用父类的同名方法
        # 默认调用本身同名方法函数
        print('调用父级同名方法：')
        AObj.__init__(self, self.name, self.info)
        AObj.event(self)

        CObj.__init__(self, self.name, self.info, self.other)
        CObj.event(self)


obj_info = BObj(name='小明', info='小明的信息', self_info_parm='继承类信息', other='其他信息')

obj_info.event()
print()
obj_info.same_name_method()

# 输出继承顺序
print(BObj.__mro__)
