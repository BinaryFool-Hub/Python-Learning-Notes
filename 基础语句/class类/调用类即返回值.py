"""
如果 __str__ 没有实现，print(obj) 会退回调用 __repr__。
只能返回字符串类型
"""


class A:
    """__str__"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        """面向用户，提供可读性好的描述。"""
        return f"A的值是 {self.value}"


print(A(10))


class B:
    """__repr__"""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        """面向开发者，提供可用于调试的精确表示，最好返回一个可以用于 eval() 还原对象的字符串。"""
        return f"B的值是 {self.value}"


print(B(10))
