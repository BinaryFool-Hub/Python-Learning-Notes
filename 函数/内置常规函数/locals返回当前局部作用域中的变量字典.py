"""
locals()用于返回局部作用域中的变量字典，函数传入的变量也属于，外部变量才不属于
"""

info = "notes"
msg = '信息'


def index(data):
    title = "小明"
    age = 19

    print(locals())


if __name__ == '__main__':
    index(info)
