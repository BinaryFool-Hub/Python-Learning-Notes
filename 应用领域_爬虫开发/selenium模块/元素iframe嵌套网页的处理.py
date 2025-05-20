from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://music.163.com/#/song?id=1450083773')

"""切换进入嵌套网页"""
# 方式1: 根据嵌套网页标签的索引切换进入 索引值从0开始； 索引值不能超出当前已有的嵌套网页数量，否则报错
# driver.switch_to.frame(0)

# 方式2: 根据嵌套网页的 <iframe> 标签切换进入到嵌套网页
iframe = driver.find_element(By.CSS_SELECTOR, '#g_iframe')
driver.switch_to.frame(iframe)
print(driver.page_source)  # 获取元素代码

print("------------------------------")

# 从子iframe切换到父iframe
driver.switch_to.parent_frame()
print(driver.page_source)  # 获取元素代码

"""
嵌套网页常见于登录注册页面
"""
