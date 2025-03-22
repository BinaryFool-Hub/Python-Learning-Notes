"""
减少线程创建和销毁的开销。
控制并发线程数量，防止资源耗尽。
提高任务响应速度。
统一管理任务调度。
避免资源竞争，提高程序稳定性。


"""

import concurrent.futures
import time
import random


def job(n):
    time.sleep(random.randint(0, 4))  # 模拟任务时间
    print(f"第{n}个运行完成")


"""第一种创建"""
# 创建一个线程池，限制最大线程工作数
ex = concurrent.futures.ThreadPoolExecutor(max_workers=5)
for i in range(20):
    ex.submit(job, i)  # 把任务下发给线程池处理

ex.shutdown()  # 等待内容全部执行完毕，关闭后台资源占用

"""第二种创建，不需要写关闭操作"""
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     for i in range(20):
#         executor.submit(job, i)  # 把任务下发给线程池处理
