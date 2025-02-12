def _continue():
    """
    跳过当前循环 continue 下面同层级的代码
    :return:
    """
    for i in range(5):
        print(i)
        continue
    else:
        print('正常结束')


def _break():
    """
    第一次循环遇到 break ,非正常结束，不会执行 else
    :return:
    """
    for i in range(5):
        print(i)
        break
    else:
        print('非正常结束')


if __name__ == '__main__':
    _continue()
    _break()
