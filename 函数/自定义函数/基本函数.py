# 基础函数
def fun():
    print("hello word!")


fun()


# 使用def 定义一个名字为 fun的函数，
# 第一个参数为param1传入的是字符型，第二个参数param2传入的是int型，可不写
# 返回值为None，可不写->None
def fun1(param1: str, param2: int) -> None:
    return None


# 调用函数
fun1('1', 1)


# 不定长参数
# args 用于接收自定义参数外的值，返回元组
# kwargs 用于接受自定义参数外的参数值和参数，返回字典
# 位置：args需要放在kwargs前面，这两者参数都需呀放在自定义参数后面
def fun1(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)


fun1(1, 1, 1, 1, 4, 4, '222', anc=1, pam='dddd')
