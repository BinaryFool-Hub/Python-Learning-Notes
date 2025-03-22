# 使用 pyinstaller 打包会出现路径问题，使用下面函数即可获取打包后的路径

import sys
import os


def resource_path(relative_path):
    """
    获取资源的路径
    :param relative_path: 项目的相对路径
    :return: 可以使用的正确路径
    """
    if hasattr(sys, '_MEIPASS'):  # 如果有该属性就
        # 打包后的资源路径
        return os.path.join(sys._MEIPASS, relative_path)

    return relative_path
