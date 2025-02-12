import time

# strftime 格式化输出时间
# time.localtime() 获取本地时间，里面不写时间戳则自动转换为当前时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 传入 t_ 把时间戳转换成可读的时间模式
t_ = 1737877848.385091
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_)))
