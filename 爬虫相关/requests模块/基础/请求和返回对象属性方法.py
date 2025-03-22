import requests

url = 'https://movie.douban.com/top250'

headers = {
    'authority': 'movie.douban.com',
    'Referer': 'https://www.baidu.com/link?url=KbThaYpxi-swWTM0wPfyxEdgWYCpw02U8naXraIxI3wtIHklB8x6MOBVj9jLxwfz&wd=&eqid=d4f5ab82006d46df00000006671b899c',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

response = requests.get(url=url, headers=headers)  # 响应对象

"""请求体中的"""
print(response.request.url)  # 查看请求体中 url 地址
print(response.request.headers)  # 查看请求体中请求头信息, requests模块在请求时,会自动带上常见的请求字段
print(response.request.method)  # 查看请求体中请求方法

"""响应体中的"""
print(response.text)  # 返回的是没有经过浏览器渲染的数据 网页源代码
print(response.content)  # 获取响应体的二进制数据  图片 视频 音频 都属于二进制类型
# print(response.json())   # 获取响应体的json数据, 如果数据不是json数据, 使用json()方法提取会报错
print(response.headers)  # 查看响应体的响应头信息
print(response.encoding)  # 指定响应体编码
print(response.apparent_encoding)  # 自动识别响应体编码
print(response.cookies.get_dict())  # # 获取响应体的 cookies 字段信息, 得到的是 RequestsCookieJar对象  get_dict() 转字典
print(response.url)  # 获取响应体的url地址
print(response.status_code)  # 获取响应体的状态码
