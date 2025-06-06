"""
@staticmethod 是用来定义静态方法的装饰器

没有 self 或 cls 参数
不依赖对象实例或类本身，只是封装在类里的普通函数
主要用于类中的工具函数
"""


class MathTools:
    @staticmethod
    def add(a, b):
        return a + b


obj = MathTools()
print(obj.add(0, 1))

print(MathTools.add(3, 5))  # 可以不需要创建对象
