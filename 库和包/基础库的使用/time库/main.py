import time

# strftime 格式化输出时间
# time.localtime() 里面不传入时间戳则获取本地时间，如果传入就处理传入的时间
t_ = 1737877848.385091
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_)))

# 时间戳转换为绝对时间，就不需要格式化输出，但是返回的是英文信息
t_ = 1519191231.0
print(time.ctime(t_))  # 不写的话默认本地时间戳传入
