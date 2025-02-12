import requests

"""
ConnectTimeout   链接超时
默认requests模块只要在请求途中没有其他因素干扰, 会等待180s响应, 超过就报错

timeout  自己设置响应时间, 超过也会报错"""

url = 'https://www.bilibili.com'

# timeout=0.00001   设置响应时间, 单位/秒, 如果响应超过设置的时间就会报错
response = requests.get(url=url, timeout=0.00001)
print(response)
