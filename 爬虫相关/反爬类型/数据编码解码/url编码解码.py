"""
http协议默认对与中文是不支持的, 会自动把中文转化成 URL编码
url编码的组成: (%  + 字母 + 数字)
下面两个方式都可以，requests是继承urllib模块的
"""

from urllib import parse
import requests

"""方式一"""
# 编码
a = parse.quote('中国欢迎你')
print(a)

# 解码
b = parse.unquote(a)
print(b)

"""方式二"""
c = requests.utils.quote('中国欢迎你')
print(c)

d = requests.utils.unquote(c)
print(d)
