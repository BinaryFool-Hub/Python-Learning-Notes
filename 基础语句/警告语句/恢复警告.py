import warnings

# 恢复所有警告
warnings.resetwarnings()

# 单独回复某个警告
warnings.filterwarnings("default", category=UserWarning)
