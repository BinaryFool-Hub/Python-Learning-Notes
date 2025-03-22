"""
位置参数永远在关键字参数前面
args 在 kwargs前面

"""


def args_parameter(*args):
    """
    可接受不定长的参数
    :param args:
    :return:
    """
    print(args)


def kwargs_parameter(**kwargs):
    """
    可接受的是关键字赋值操作，返回接受的是字典形式
    :param kwargs:
    :return:
    """
    print(kwargs)


args_parameter(2, 4)
kwargs_parameter(a=1, b=2, c=3)
