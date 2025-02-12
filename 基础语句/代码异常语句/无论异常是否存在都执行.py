# finally表示的是无论是否异常都要执行的代码，都会执行
try:
    # print(name)
    print(111)

except Exception as e:
    print(e)

finally:
    print('我是finally，当try代码块下面的代码无论有没有异常都会被执行')
