"""
浅拷贝：复制对象，共享内部引用。
深拷贝：复制对象及其所有内部引用，完全独立。

选择依据：
    如果对象内部没有可变引用，浅拷贝足够。
    如果对象内部有可变引用且需独立修改，使用深拷贝。
"""

import copy


def copy_copy():
    original = [[1, 2, 3], [4, 5, 6]]
    shallow = copy.copy(original)

    shallow[0][0] = 'X'
    print(original)  # 输出: [['X', 2, 3], [4, 5, 6]]


def copy_deepcopy():
    original = [[1, 2, 3], [4, 5, 6]]
    deep = copy.deepcopy(original)

    deep[0][0] = 'X'
    print(original)  # 输出: [[1, 2, 3], [4, 5, 6]]
