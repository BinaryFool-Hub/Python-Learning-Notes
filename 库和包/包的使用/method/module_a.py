from .module_b import func_b  # 导入module_b的内容


def func_a():
    print("Function A")
    func_b()  # 调用module_b的函数
