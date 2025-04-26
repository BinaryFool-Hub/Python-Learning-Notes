import requests

url = 'http://www.baidu.com/'

# 在正常的模拟请求过程中, requests会默认自动重定向
# allow_redirects=False  阻止重定向
response = requests.get(url=url, allow_redirects=False)
print(response.status_code)
print(response.request.url)
