import json

"""
json数据最明显的特征就是双引号，但是和python的字典不同，python没有json数据类型，只有字典数据类型
字典，列表都可以进行序列化转换
如果需要使用文件的 f.write() 方法写入可以使用 f.write(json.dumps(data)),因为里面是以及序列化好的数据了，可以直接使用f.write()
"""

# 这是一个python里面的字典形式
data = {
    'name': 'andy',
    'age': 18,
    'sex': 'male'
}


def dump_or_dumps():
    """
    json.dump()     操作的是文件对象 加 s 操作的是数据
    json.dumps()    json序列化操作, 将对象转化成json字符串
    """
    # dumps
    json_str = json.dumps(data)  # 转换成json类型数据
    print(json_str)
    print(type(json_str))

    # dump
    with open('测试.json', mode='w', encoding='utf-8') as f:
        json.dump(data, f)  # 先传入python中的字典或列表数据，再传入的是文件对象，会自动进行转换和写入操作


def load_or_loads():
    global data
    """
    json.load()       操作的是文件对象 加 s 操作的是数据
    json.loads()      json反序列化操作, 将字符串转化成对象
    """

    json_str = json.dumps(data)  # 转换成json类型数据
    json_obj = json.loads(json_str)  # 转换成了python的字典形式
    print(json_obj)
    print(type(json_obj))

    with open('测试.json', mode='r', encoding='utf-8') as f:
        data = json.load(f)  # 传入的是文件对象，会自动进行转换和读取操作
        print(data)
        print(type(data))


def indent_parameter():
    """
    当我们写入json数据的时候会发现编码不正确和无格式化操作
    编码和缩进操作
    encoding
    ensure_ascii
    indent
    """
    with open('测试1.json', mode='w', encoding='utf-8') as f:  # encoding 是指定编码，utf-8是Linux和Windows通用的编码
        # 我在下面使用了传入文件对象的操作。ensure_ascii 是取消默认编码，使用我们文件指定的utf-8编码,indent是指定格式化代码和缩进块
        json.dump(data, f, ensure_ascii=False, indent=2)


dump_or_dumps()
load_or_loads()
indent_parameter()
