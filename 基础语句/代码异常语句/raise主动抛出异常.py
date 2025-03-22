def div(a, b):
    if b == 0:
        raise Exception('这个异常是我自己手动抛出的')  # 主要是用异常提醒或标记 增加自己的印象，也可以捕获，使用 Exception


# 调用函数执行里面的代码逻辑
div(6, 0)
div(10, 2)
