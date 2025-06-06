"""
__repr__

- 用于定义 开发者友好 的表示。
- 当你在交互式环境中直接输入对象，或者使用 repr(obj) 时调用。
- 目的是尽可能准确地表示对象，通常应返回可以用来重建对象的字符串。
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


p = Person("Alice", 30)
print(repr(p))  # 输出：Person(name='Alice', age=30)
