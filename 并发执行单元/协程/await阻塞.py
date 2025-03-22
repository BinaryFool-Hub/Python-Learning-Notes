import asyncio
import time


async def other():
    print('协程任务正在执行')
    await asyncio.sleep(2)  # 让对象进行等待 await支持在这个休眠时间去调度其他的任务的
    print('协程任务已经完成')
    return '这是个当前的协程任务'


async def main():
    start = time.time()  # 记录开始的时间
    print('正在执行的协程任务,other')

    # await 拿到res返回值的时候才会解开阻塞去执行下一个任务res1
    # 任务分为3个状态(睡眠状态(任务还没有开始)   准备状态(await挂起操作 随时可以执行)   (完成阶段,执行完了)task对象异步的并发

    """阻塞"""
    # res = await other()
    # res1 = await other()

    """阻塞解决方法"""
    # 创建task对象
    task1 = asyncio.create_task(other())
    task2 = asyncio.create_task(other())
    # future是task的父类，future具有更多的功能，但是很复杂，task进行了二次封装，更便捷的使用
    # 创建future对象
    # task1 = asyncio.ensure_future(other())
    # task2 = asyncio.ensure_future(other())
    res = await task1
    res1 = await task2

    # await 将任务状态由睡眠------> 挂起(准备阶段)
    print('当前协程任务的返回值', res, res1)
    print('花费的时间', time.time() - start)


# 运行协程函数
asyncio.run(main())
