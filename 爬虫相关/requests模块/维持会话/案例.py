import time
import requests
import ddddocr

ocr = ddddocr.DdddOcr(beta=True, show_ad=False)  # ddddocr识别验证码
reqs_obj = requests.Session()  # 初始化请求obj
time_info = str(int(time.time() * 1000))  # 时间戳

# 更新默认的headers
reqs_obj.headers.update({
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
})

# 自定义请求头的追加
headers = {
    'self_event': 'customize',
    'self_event1': 'customize1',
}


def get_img_code():
    """
    获取验证码
    :return:
    """
    url = 'http://159.75.103.8:5000/login/captcha'

    params = {
        'image_code': time_info
    }

    response = reqs_obj.get(url=url, params=params, headers=headers)

    code_result = ocr.classification(response.content)

    print(response.request.headers)

    return code_result


# 登录操作，也是使用reqs_obj
login_url = 'http://159.75.103.8:5000/api/private/v1/login'
json_data = {
    'image_code': time_info,
    'username': "admin",
    'password': "123456",
    'captcha_code': get_img_code()
}

# 删除一个请求头
del headers['self_event1']
login_response = reqs_obj.post(url=login_url, json=json_data, headers=headers)

print(login_response.json())
print(login_response.request.headers)
