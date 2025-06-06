"""
__dict__属性常用于调试作用，解包类里面的数据有哪些

不止自己定义的类可以解包，第三方类也可以
"""


class A(object):
    info = 10  # 不在解包范围

    def __init__(self):
        self.a = 1
        self.b = 3

    def fun(self):
        self.c = 9  # 当方法被调用执行的时候才会有这个变量，否则无


obj = A()
print(obj.__dict__)
