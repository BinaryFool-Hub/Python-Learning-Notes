"""
yield 相当于是一个断点，next执行才会释放继续执行/obj.__next__()，在下一个yield又会断住
协程的本质就是独立的线程，没有资源竞争
"""


def fun():
    print("当前是一个生成器函数")
    while True:
        yield "这是生成器函数的返回值"


# 返回的不是函数调用，而是对象，yield是生成器函数的标志
# print(fun())


# 直接调用
info_obj = fun()
print(next(info_obj))
print(next(info_obj))
print(info_obj.__next__())
