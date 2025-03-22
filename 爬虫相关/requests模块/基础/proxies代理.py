import requests

# 代理，流量走了指定的ip，需要自行更改
proxies = {
    "http": "http://" + '192.1.1.1:111',
    "https": "http://" + '192.1.1.1:111',
}

response = requests.get('https://www.baidu.com/', proxies=proxies)

print(response)
