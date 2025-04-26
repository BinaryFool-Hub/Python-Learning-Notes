"""
cookies是有时效性  不同的网址时间不一样 2分钟 半小时

cookies有三种 放headers里面   单独cookies   构建每个片段

方式1不行就用方式2, 方式2不行就用方式3
"""

import requests


def fun1():
    """ 方式1: cookies可以放请求头里面 """
    headers = {
        'Cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1740848341; sessionid=ipg8s78kdkdsqp12bgkgy46n3xw3j6fk'
    }
    response = requests.post(url='https://example.com', headers=headers)


def fun2():
    """ 方式2: cookies可以构建字典对象, 使用cookies关键字提交请求 """
    cookies = {
        'Cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1740848341; sessionid=ipg8s78kdkdsqp12bgkgy46n3xw3j6fk'
    }
    response = requests.post(url='https://example.com', cookies=cookies)


def fun3():
    """ 方式3: 构建cookies的每个片段"""
    cookies = {
        "Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3": "1740848341",
        "sessionid": "ipg8s78kdkdsqp12bgkgy46n3xw3j6fk"
    }
    response = requests.post(url='https://example.com', cookies=cookies)
