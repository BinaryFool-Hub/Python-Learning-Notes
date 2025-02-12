# 捕获特定异常
try:
    print(10 / 0)
    print(name)

except (NameError, ZeroDivisionError) as e:  # 指定异常的名字进行捕获，可以指定单个或者多个
    print('有错误')
    print(e)

# 捕获所有异常
try:
    print(10 / 0)
    print(name)

except Exception as e:  # 捕获所有的异常赋值给 e 然后进行打印输出
    print(e)
