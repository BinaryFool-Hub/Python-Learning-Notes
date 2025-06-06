"""
__str__

- 用于定义 用户友好 的字符串表示。
- 当你使用 print(obj) 或 str(obj) 时调用。
- 目的是让输出更易读，适合展示给用户。
- 如果没有定义__str__则会调用__repr__
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


p = Person("Alice", 30)
print(p)  # 输出：Person(name=Alice, age=30)
