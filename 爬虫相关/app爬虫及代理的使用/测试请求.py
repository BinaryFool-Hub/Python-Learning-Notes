import requests

url = 'http://www.jokes8.com/jokes8/joke/getJokeListByTypeV2'
headers = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "okhttp-okgo/jeasonlzy",
    "Host": "jokes8.com",
    "Authorization": "10000,10000,10000,10000,2.4.8,248,1739351907981,,,,,dcff1bcb503965a0dfde1fe27e3ad3f4,true",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "34",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

data = {
    "pageSize": "20",
    "pageIndex": "1",
    "jokeType": "4"
}
response = requests.post(url=url, headers=headers, data=data)
for item in response.json()["data"]:
    print(item['content'])
    print()
