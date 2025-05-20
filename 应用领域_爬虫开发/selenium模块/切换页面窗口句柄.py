import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
点击后自动打开的页面, 在浏览器中会自动定位到新页面
但是句柄还是在之前的页面, 数据也是之前页面的数据
如果数据操作需要操作新页面, 那么需要切换窗口句柄<第一次切换只是切换数据>
后续如果需要切换到之前的页面, 也是使用切换窗口句柄的方式实现<切换窗口>
"""

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://www.douban.com/')

# 点击进入到  "豆瓣读书"
# 会新打开一个网页页面, 在浏览器中也会自动定位到新窗口页面, 但是数据和句柄还是之前窗口的数据
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.lnk-book').click()
# 展示源码数据
print(driver.page_source)

print(driver.window_handles)  # 获取当前浏览器有多少个页面窗口信息

# 切换窗口和句柄
driver.switch_to.window(driver.window_handles[-1])
# 展示源码数据
print(driver.page_source)

"""
想要操控哪个窗口就切换到哪个窗口去
"""

driver.close()  # 关闭当前窗口句柄的页面

print(driver.window_handles)  # 获取当前浏览器有多少个页面窗口信息，因为上面关闭了一个，就剩下一个窗口信息
time.sleep(2)
