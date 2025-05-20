import time
from selenium.webdriver import Keys  # 键盘事件功能
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

"""键的大小写不规定"""

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')

# 定位百度的输入框
input_obj = driver.find_element(By.CSS_SELECTOR, '#kw')
input_obj.send_keys('python')
time.sleep(1)

# 键盘事件只能通过标签对象调用
input_obj.send_keys(Keys.CONTROL, 'A')  # 全选键
time.sleep(1)

input_obj.send_keys(Keys.CONTROL, 'c')  # 复制键
time.sleep(1)

input_obj.send_keys(Keys.CONTROL, 'x')  # 剪切键
time.sleep(1)

driver.get('https://www.sogou.com/')
sougou_input = driver.find_element(By.CSS_SELECTOR, '#query')
sougou_input.send_keys(Keys.CONTROL, 'v')  # 粘贴

# 搜索
search_input = driver.find_element(By.CSS_SELECTOR, '#stb')
search_input.send_keys(Keys.ENTER)  # 回车确定

input()
