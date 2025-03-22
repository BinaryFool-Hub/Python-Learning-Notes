import os


def getcwd_method():
    # getcwd 方法

    # 返回 py 文件当前的绝对路径
    result = os.getcwd()
    print(result)


def rmdir_method():
    # rmdir 方法

    name = 'file_name'

    # 删除空文件夹，不指定路径默认当前目录
    os.rmdir(name)


def mkdir_method():
    # mkdir 方法

    name = '文件夹名字'

    # 创建文件夹，如果只传入文件名则创建的是在当前目录，文件夹存在报错
    os.mkdir(name)


def chdir_method():
    # chdir 方法

    # 切换工作目录
    os.chdir('测试目录')

    print(os.getcwd())


def exists_method():
    # 判断文件夹/文件是否存在

    result = os.path.exists('测试目录')
    print(result)

    result = os.path.exists('测试目录1.txt')
    print(result)


def splitext_method():
    # 将文件名和后缀分开，元组返回

    result = os.path.splitext('测试目录/测试目录.txt')
    print(result)


def basename_method():
    # 单独获取文件名字，很好的兼容了mack，Linux，window系统之间的路径连接符
    result = os.path.basename('测试目录/测试目录.txt')
    print(result)


def abspath_method():
    # 获取当前目录的绝对路径

    result = os.path.abspath('.')  # 当前目录
    result1 = os.path.abspath('..')  # 上一级目录
    print(result)
    print(result1)


def isfile_isdir_method():
    # 判断是否为一个文件
    print(os.path.isfile('测试目录/测试目录.txt'))

    # 判断是否为一个文件夹
    print(os.path.isdir('测试目录'))


def rename_method():
    # 测试目录/文件夹
    os.rename('测试目录/测试目录', '测试目录/测试目录111')  # 文件夹
    os.rename('测试目录/测试目录.txt', '测试目录/新名字.txt')  # 文件


def link_method():
    """
    os.link() 函数用于在文件系统中创建一个硬链接。
    硬链接是一个指向文件物理存储位置的引用，多个硬链接可以指向同一个文件，它们共享相同的数据块，并且对其中任何一个链接所做的更改都会反映到其他链接上。
    注意：
        确保源文件或目录存在，否则会抛出 FileNotFoundError 异常。
        目标路径不能已经存在，否则会抛出 FileExistsError 异常。
        在 Windows 系统中，创建硬链接需要管理员权限，并且要注意不能对目录创建硬链接。
        在类 Unix 系统中，虽然可以对目录创建硬链接，但不建议这样做，因为可能会导致文件系统出现问题。
    :return:
    """
    # 源文件路径
    source_file = r"C:\Users\BinaryFool\Desktop\新建文件夹\新建文件夹\新建 文本文档.txt"
    # 目标硬链接路径
    target_link = r"C:\Users\BinaryFool\Desktop\新建文件夹\新建 文本文档.txt"

    try:
        os.link(source_file, target_link)
        print(f"硬链接 {target_link} 创建成功。")
    except FileExistsError:
        print(f"目标路径 {target_link} 已存在。")
    except PermissionError:
        print("没有足够的权限创建硬链接，请以管理员身份运行脚本。")
    except OSError as e:
        print(f"创建硬链接时发生错误: {e}")
