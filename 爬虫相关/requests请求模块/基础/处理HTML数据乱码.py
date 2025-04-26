import requests

url = 'http://www.baidu.com'
response = requests.get(url=url)
print('编码未处理前：', response.text)

response.encoding = response.apparent_encoding
# response.encoding = 'utf-8'
"""
自动识别常见的乱码变为正确的编码并且进行重新编码

response.encoding --> 重新编码
response.apparent_encoding --> 自动识别常见的乱码变为正确的编码

response.encoding = 'utf-8'
-- 和第`response.apparent_encoding`行意思相同，缺点就是需要自动判断编码。而如果使用 `response.apparent_encoding` 则会自动识别常见的编码

"""

print('该编码为：', response.encoding)
print('编码已处理后：', response.text)
