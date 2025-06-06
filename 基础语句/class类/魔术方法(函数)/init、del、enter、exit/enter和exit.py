"""
__enter__(self):
    在进入 with 代码块前自动执行。
    通常用于初始化资源（如打开文件、建立连接）。
    返回值会赋给 as 后的变量。

__exit__(self):
    在退出 with 块时自动执行（无论是否抛异常）。
    通常用于清理资源（如关闭文件、断开连接）。
    返回 True 可以吞掉异常，否则异常会继续抛出。
"""


class Demo:
    def __enter__(self):
        print("进入")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出")
        if exc_type:
            print(f"捕获异常: {exc_type.__name__}")
        return True  # 抑制异常传播


with Demo() as d:
    print("处理中")
    print(d)
    1 / 0  # 会被 __exit__ 捕获
