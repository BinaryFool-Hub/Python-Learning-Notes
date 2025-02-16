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
