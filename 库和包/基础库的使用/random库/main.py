import random


def random_():
    # 返回随机 0-1 之间小数，不接收传参数
    result = random.random()
    print(result)


def randint_():
    # 返回随机整数，需要传入范围（起始位和结束位都包含在随机范围）
    result = random.randint(1, 2)
    print(result)


def uniform_():
    # 返回随机小数，需要传入范围，返回之间的小数（包含起始位置）
    result = random.uniform(1, 2)
    print(result)


def choice_():
    # 随机选择一个可遍历对象的元素
    # a = "niidf" # 也可以字符串
    a = [1, 3, 5, 6, 77, 78]
    result = random.choice(a)
    print(result)


def shuffle_():
    # 打乱可遍历对象的顺序，不可字符串
    a = [1, 3, 5, 6, 77, 78]
    random.shuffle(a)
    print(a)


def seed_():
    """
    随机种子
    随机种子作用在于，当再次播种种子的时候结果还是相同
    相当于同一个种子播种出来的果实都是一样的
    """

    # 第一次播种
    random.seed(1)  # 以0为做随机种子（自定义）
    result = random.randint(1, 8)  # 不一定是随机整数，也可随机小数
    print(result)

    result = random.randint(1, 8)  # 不一定是随机整数，也可随机小数
    print(result)

    # 再次播种，结果就是第一次播种的，里面播种的参数需要相同，不然是新的种子
    random.seed(1)  # 以0为做随机种子（自定义）
    result = random.randint(1, 8)  # 不一定是随机整数，也可随机小数
    print(result)

    result = random.randint(1, 8)  # 不一定是随机整数，也可随机小数
    print(result)


if __name__ == '__main__':
    seed_()
