import threading
import time


def fun(n):
    time.sleep(3)
    print(f"当前线程{n}执行完成 ")


for i in range(15):
    th_fun = threading.Thread(target=fun, args=(i,))
    th_fun.start()

print("子线程分配完毕")

"""统计当前线程活跃个数：总数 = 主线程 + 子线程"""
number = threading.active_count()
print(f"当前线程活跃个数: {number}")

"""当前运行的线程"""
th_info = threading.enumerate()
print(f"当前运行的线程：{th_info}")
