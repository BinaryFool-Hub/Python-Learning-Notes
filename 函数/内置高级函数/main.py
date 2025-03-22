def map_fun():
    """
    map 函数是处理数据，内部会进行遍历
    :return:
    """
    list1 = [1, 4, 67, 8, 9]

    def fun(data):
        return data + 5

    result = map(fun, list1)  # 默认子啊底层进行遍历然后执行函数
    print(list(result))


def map_and_lambda_fun():
    """
    map 函数是处理数据，内部会进行遍历
    :return:
    """
    list1 = [1, 4, 67, 8, 9]

    result = map(lambda data: data + 5, list1)  # 默认子啊底层进行遍历然后执行匿名函数，这样就可以简写一个单独的函数
    # - 但 lambda 匿名函数只能处理简单的
    print(list(result))


def zip_fun():
    list1 = [1, 4, 67, 8, 9]
    list2 = [9, 5, 33, 0, 222, 33]
    list3 = [9, 5, 33, 0, ]
    result = zip(list1, list2, list3)  # 会择优考虑长度最小的，剩下的则不进行处理
    # - 该函数是针对于数据打包

    print(list(result))


def filter_fun():
    """
    filter 函数会自动筛选出符合条件的数据
    :return:
    """
    list1 = [1, 4, 67, 8, 9]

    def fun(data):
        if data == 1 or data == 4:
            return data

    result = filter(fun, list1)  # 会底层遍历然后返回给数据处理函数进行返回
    print(list(result))


def filter_and_lambda_fun():
    """
    filter 函数会自动筛选出符合条件的数据
    :return:
    """
    list1 = [1, 4, 67, 8, 9]

    result = filter(lambda data: data == 1 or data == 4, list1)  # 会底层遍历然后返回给数据处理函数进行返回
    print(list(result))


map_fun()
map_and_lambda_fun()
zip_fun()
filter_fun()
filter_and_lambda_fun()
