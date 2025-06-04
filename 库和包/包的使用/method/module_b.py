from .module_a import func_a  # 导入module_a的内容


def func_b():
    print("Function B")
    func_a()  # 调用module_a的函数
