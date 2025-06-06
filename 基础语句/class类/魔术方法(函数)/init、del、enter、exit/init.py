"""
init魔法属性
用于初始化类(打开文件和传入变量等操作)
只会在类被实例化时调用一次
"""


class A(object):
    def __init__(self, data):
        self.data = data  # 初始化类的数据
        print(self.data)


if __name__ == '__main__':
    A('数据')  # 实例化的时候会执行init方法
