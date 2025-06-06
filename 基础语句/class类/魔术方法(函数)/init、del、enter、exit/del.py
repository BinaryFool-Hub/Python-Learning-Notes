"""
del魔法属性
用于在对象销毁前处理事件
但注意：
    __del__ 的调用时间不确定（取决于垃圾回收），不可靠做资源释放
    推荐用 with + __enter__ / __exit__ 管理资源更安全
"""


class A(object):
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 被创建")

    def __del__(self):
        print(f"{self.name} 被销毁")


if __name__ == '__main__':
    p = A("小明")
    del p  # 触发 __del__
