# https://bark.day.app/#/

import requests

your_key = '你的iPhone的key'
"""注解
输入你的iPhone的key即可
"""

headers = {
    'Content-Type': 'application/json; charset=utf-8',
}

json_data = {
    'body': '测试内容',
    'title': '测试标题',
}

response = requests.post(f'https://api.day.app/{your_key}', headers=headers, json=json_data)

print(response.json())
