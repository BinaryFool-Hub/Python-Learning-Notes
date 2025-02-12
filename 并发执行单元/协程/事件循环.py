import asyncio


# 任务一
async def fun1():
    for i in range(5):
        print('我是fun1的协程函数')
        await asyncio.sleep(2)  # 异步休眠结合await进行等待的

    return '执行完成'


# 任务二
async def fun2():
    for i in range(5):
        print('我是fun2的协程函数')
        await asyncio.sleep(2)  # 异步休眠结合await进行等待的

    return '执行完成'


"""3.7之前的执行方法"""
# # 创建事件循环的对象 用于去完成协程任务
# loop = asyncio.get_event_loop()
#
# task = [fun1(), fun2()]  # 保存在列表里面
#
# # 执行协程函数
# result = loop.run_until_complete(asyncio.wait(task))  # 这个方法是需要传递可迭代对象的
# for item in result[0]:
#     print("返回结果：", item.result())
#
# # 单独执行一个
# result = loop.run_until_complete(fun1())
# print("返回结果", result)


"""3.7之后的简便方法，但是前面的方法也可以使用"""
task = [fun1(), fun2()]  # 保存在列表里面

result = asyncio.run(asyncio.wait(task))  # 这个方法是需要传递可迭代对象的
for item in result[0]:
    print("返回结果：", item.result())

# 单独执行一个
# result = asyncio.run(fun1())
# print("返回结果", result)
