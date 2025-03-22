# 断言就是我提前知道错误的类型 针对这个类型进行错误的抛出
def div(a, b):
    # assert  后面的布尔结果为False就会触发断言,后面的布尔结果为True就不会触发断言
    print(b != 0)
    assert b != 0, 'b不等于0'
    return a / b


print(div(7, 2))
print(div(8, 0))
