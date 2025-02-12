def open_fun():
    # open 函数

    file = open(file='file.txt', mode='w')
    file.write('123456')

    # 需要关闭文件 防止信息的泄露
    file.close()


def seek_fun_about_file():
    # 因为写入进去的时候光标在后面，所以在读取的时候光标也需要在开头才能读取完整
    with open(file='测试目录/测试文件.txt', mode='w+', encoding='utf-8') as file:
        file.write('测试内容')
        file.seek(0)  # 光标置顶
        print(file.read())

        file.seek(0, 2)  # 光标移至末尾,不懂看下面详情
        file.write('测试内容')

        file.seek(0)  # 光标置顶
        print(file.read())


def self_file():
    # 返回当前文件的文件名
    print(__file__)


self_file()

"""
file.seek(offset, whence) 是 Python 文件操作中用于移动文件指针（光标）的函数。其中：

offset：偏移量（以字节为单位）。
whence：参考位置（默认是 0）。
0（io.SEEK_SET）：从文件开头算起（默认）。
1（io.SEEK_CUR）：从当前位置算起。
2（io.SEEK_END）：从文件末尾算起。
所以，file.seek(0, 2) 表示：

offset=0（偏移 0 字节）。
whence=2（从文件末尾计算）。
作用：将光标移动到文件末尾，便于在末尾追加内容。
"""
