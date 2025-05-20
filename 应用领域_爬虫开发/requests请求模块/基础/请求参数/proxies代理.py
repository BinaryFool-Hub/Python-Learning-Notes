"""
代理，流量走了指定的ip，需要自行更改

该网址用户检测所在区域的公网请求ip：https://httpbin.org/ip
"""

import requests


def fun1():
    """基本代理设置"""
    proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890'
    }

    response = requests.get('https://httpbin.org/ip', proxies=proxies)
    print(response.json())  # 应该显示你的代理IP而不是本地IP


def fun2():
    """如果需要认证的代理"""
    proxies = {
        'http': 'http://username:password@127.0.0.1:7890',
        'https': 'http://username:password@127.0.0.1:7890'
    }

    response = requests.get('https://httpbin.org/ip', proxies=proxies)
    print(response.json())  # 应该显示你的代理IP而不是本地IP


def fun3():
    """快捷写法（如果http/https使用相同代理）"""
    proxies = {
        'all': 'http://127.0.0.1:7890'
    }

    response = requests.get('https://httpbin.org/ip', proxies=proxies)
    print(response.json())  # 应该显示你的代理IP而不是本地IP


def fun4():
    """使用会话保持（推荐）"""
    session = requests.Session()

    session.proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890'
    }

    response = session.get('https://httpbin.org/ip')
    print(response.json())  # 应该显示你的代理IP而不是本地IP


if __name__ == '__main__':
    fun4()
