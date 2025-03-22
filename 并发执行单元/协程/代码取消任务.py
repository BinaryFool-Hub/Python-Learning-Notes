import asyncio


async def work(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print(f"休眠完成")
    return seconds


async def main():
    long_task = asyncio.create_task(work(10))
    seconds_elapsed = 0

    while not long_task.done():
        print("检测到任务尚未完成，一秒钟之后继续检测")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        # 时间超过 5 秒，取消任务
        if seconds_elapsed == 5:
            """取消任务"""
            long_task.cancel()

    try:
        await long_task  # 如果任务提前取消，是获取不到结果的，会报错
    except asyncio.exceptions.CancelledError as e:  # 指定异常名字进行捕获
        print('任务被取消了', e)


asyncio.run(main())
