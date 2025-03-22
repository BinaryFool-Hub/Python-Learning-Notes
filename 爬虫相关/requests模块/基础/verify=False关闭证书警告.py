import requests

# 证书警告关闭
"""
警告信息：InsecureRequestWarning
"""
requests.packages.urllib3.disable_warnings()

"""
没有证书的网址需要正常请求会报错，所以声明添加无证书
requests.exceptions.SSLError: HTTPSConnectionPool(host='p.qqan.com', port=443): Max retries exceeded with url: /up/2019-7/2019071108020877477.jpg (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1007)')))
"""
response = requests.get('https://p.qqan.com/up/2019-7/2019071108020877477.jpg', verify=False)

print(response)
