"""
减少进程创建和销毁的开销。
充分利用多核CPU，适合CPU密集型任务。
提供资源隔离，避免任务间干扰。
控制并发进程数量，防止资源耗尽。
统一管理任务调度。
"""

import concurrent.futures
import time
import random


def job(n):
    time.sleep(random.randint(0, 4))  # 模拟任务时间
    print(f"第{n}个运行完成")


if __name__ == '__main__':
    """第一种创建"""
    # 创建一个进程池，限制最大进程工作数
    ex = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    for i in range(20):
        ex.submit(job, i)  # 把任务下发给进程池处理

    ex.shutdown()  # 等待内容全部执行完毕，关闭后台资源占用

    """第二种创建，不需要写关闭操作"""
    # with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    #     for i in range(20):
    #         executor.submit(job, i)  # 把任务下发给进程池处理
