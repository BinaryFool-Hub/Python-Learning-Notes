import requests

"""
http协议默认对与中文是不支持的,会自动把中文转化成 URL编码,在使用requests请求的时候可以不进行url编码操作
url编码的组成: (%  + 字母 + 数字)
"""

# requests.utils.quote('中文')  将中文进行url编码
print(requests.utils.quote('风景'))
print(requests.utils.quote('湖泊'))

# requests.utils.unquote('url编码')  将url编码进行解码
print(requests.utils.unquote('%E9%A3%8E%E6%99%AF'))
print(requests.utils.unquote('%E6%B9%96%E6%B3%8A'))
