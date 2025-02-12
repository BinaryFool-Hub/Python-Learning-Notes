list1 = ['asdfsd', 'dfhgdfg', 345, True, False, 3.2, 'asfasdfasdfasdfs', 'dfhgdfg']

list2 = ['l,sdlmfamfd', '566', 2345435]

list3 = [65, 6, 6, 5, 88, 0, 0.8, ]
list4 = ['g', 'j', 'i', 'asdfg']


def list_extend():
    list1.extend(list2)  # 追加到第一个 list1 中
    print(list1)


def list_insert():
    list1.insert(0, '111')  # 第一个是索引，添加到哪里
    list1.insert(-1, '333')  # 第一个是索引，添加到哪里
    print(list1)


def list_pop():
    list1.pop(0)  # 里面接受数据删除的索引
    list1.pop(-1)  # 里面接受数据删除的索引
    list1.pop()  # 不填写则删除最后一个
    print(list1)


def list_remover():
    list1.remove(345)  # 支持指定数据的删除
    list1.remove('asdfsd')  # 支持指定数据的删除

    print(list1)


def list_index():
    index_num = list1.index('dfhgdfg')  # 里面传入数据，返回的是该数据的索引
    print(index_num)


def list_del():
    del list1[0]  # 删除指定列表中的索引数据
    print(list1)


def list_reverse():
    list1.reverse()  # 逆置，把数据反转过来
    print(list1)


def list_stor():
    """
    不能数字和str进行比较排序，str比较的是ASCII值的大小
    :return:
    """
    list3.sort()  # 排序 他是可以默认升序从小到大进行排列
    list4.sort()  # 排序 他是可以默认升序从小到大进行排列
    print(list3)
    print(list4)

    list3.sort(reverse=True)  # 这是降序，默认为False
    list4.sort(reverse=True)  # 这是降序，默认为False
    print(list3)
    print(list4)


def list_count():
    num = list1.count('dfhgdfg')  # 用于统计列表中出现的个数，返回统计的个数
    print(num)


def list_append():
    list1.append('追加的字符，也可以是int等')  # 用于追加到列表的最后面
    print(list1)


def list_add_index():
    for i in list(enumerate(list1)):
        print(i)


def list_dict_sort():
    students = [
        {'name': 'TOM', 'age': 20},
        {'name': 'ROSE', 'age': 19},
        {'name': 'Jack', 'age': 22}
    ]

    def key_fun(data):
        return data['age']

    students.sort(key=key_fun)
    print(students)


def list_clear():
    print(list4)
    list4.clear()
    print(list4)


def sys_reversed_fun():
    print(list4)
    result = reversed(list4)
    print(list(result))


# list_extend()
# list_insert()
# list_pop()
# list_remover()
# list_index()
# list_del()
# list_reverse()
# list_stor()
# list_count()
# list_append()
# list_add_index()
# list_dict_sort()
# sys_reversed_fun()
list_clear()
