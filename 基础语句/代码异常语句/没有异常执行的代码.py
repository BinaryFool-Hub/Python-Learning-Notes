# else当try代码块下面的代码没有异常的时候我会被执行
try:
    # print(name)
    print(1111)

except Exception as r:
    print(r)

# 可以通过else是否被执行 反推我们前面的程序是否有异常
else:
    print('我是else，当try代码块下面的代码没有异常的时候我会被执行')
