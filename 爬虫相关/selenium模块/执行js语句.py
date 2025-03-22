from selenium.webdriver.chrome.service import Service
from selenium import webdriver

"""
js可以让selenium点击不到的地方进行点击操作
如果需要让js执行的语句返回值在开头使用 return 语句,不然返回none
"""

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://www.baidu.com/')

js_all = 'return document.querySelector("#bottom_layer > div > p:nth-child(6)").textContent'

result = driver.execute_script(js_all)
print(result)
