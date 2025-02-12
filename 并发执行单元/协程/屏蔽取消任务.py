import asyncio


# 屏蔽掉取消任务指令，没有取消，仍然在后台运行
# 人被取消了 但是我可以屏蔽这一条取消任务的命令   await去获取任务返回值


async def work(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print(f"休眠完成")
    return seconds


async def main():
    delay_task = asyncio.create_task(work(5))
    try:
        """asyncio.shield 可以给 task 任务添加一个屏蔽取消的方法"""
        result = await asyncio.wait_for(asyncio.shield(delay_task), 3)
        print("返回值:", result)
    except asyncio.TimeoutError:
        print("超时啦")
        print("任务是否被取消:", delay_task.cancelled())
        print("任务是否被完成:", delay_task.done())
        """任务没有内真正取消而是被屏蔽了 在后台进行运行的 一直到完成为止"""
        await delay_task
        print("任务是否被完成:", delay_task.done())


asyncio.run(main())
