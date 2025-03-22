import asyncio


async def work(x):
    print('当前接受的参数', x)
    await asyncio.sleep(x)
    return f'当前函数的返回值,{x}'


async def main():
    # 创建十个任务将十个任务提交到事件循环
    task = [asyncio.create_task(work(i)) for i in range(10)]

    # res = await asyncio.create_task(work(1))  # 这个方法只适合单个task对象

    # done ,pending = await asyncio.wait(task)
    # print(done)
    # for i in done:
    #     print(i.result())   # 接受的返回值 乱序的 代表这个是一个异步执行
    # print(bool(pending))  # False 就表明任务全部完成了  里面是空的

    # 当前的gather用于收集所有已完成任务的返回值，并且他是有顺序的
    res = await asyncio.gather(*task)
    print(res)


# 运行协程函数
asyncio.run(main())
