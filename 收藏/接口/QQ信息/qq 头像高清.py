# qq 头像高清

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}

qq_code = '123456'
url = f'https://q1.qlogo.cn/g?b=qq&nk={qq_code}&s=640'  # 备用 f'https://q2.qlogo.cn/g?b=qq&nk={qq_code}&s=640'

response = requests.get(url, headers=headers)
print(response)

with open('img.png', mode='wb') as f:
    f.write(response.content)
