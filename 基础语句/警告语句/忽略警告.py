import warnings

"""
warnings.filterwarnings("ignore")：用于控制 Python 警告的显示方式。

category=UserWarning：只忽略 UserWarning 类型的警告，其他类型的警告仍然会显示。

如果不写 category 参数默认忽略所有警告
"""

warnings.filterwarnings("ignore", category=UserWarning)
