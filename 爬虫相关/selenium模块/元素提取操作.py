import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By  # 定位器

"""实例化一个浏览器对象"""
service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.douban.com/')

# 根据标签的 id 属性值定位到标签, 返回的都是 <WebElement>  标签对象
res1 = driver.find_element(By.ID, 'anony-reg-new')
print(res1)

# 根据标签的 name 属性值定位到标签
res2 = driver.find_element(By.NAME, 'description')
print(res2)

# 根据标签的 class 属性值定位到标签
res3 = driver.find_element(By.CLASS_NAME, 'anony-nav-links')
print(res3)

# 根据标签的 文本 定位到标签<精确匹配>
res4 = driver.find_element(By.LINK_TEXT, '下载豆瓣 App')
print(res4)

# 根据标签的 文本 定位到标签<模糊匹配>
res5 = driver.find_element(By.PARTIAL_LINK_TEXT, '下载')
print(res5)

# 根据标签的名字定位到标签
# find_elements  会获取所有符合条件的标签对象, 返回一个列表
res6 = driver.find_elements(By.TAG_NAME, 'div')
print(res6)

"""xpath 和 css 定位都不支持属性提取, 和文本提取;   仅支持定位"""
# 根据 xpath 语法获取到标签  # @href text 不能使用
res7 = driver.find_elements(By.XPATH, '//a[@class="lnk-app"]')
print(res7)

# 根据 css 语法获取到标签，可以是多个
res8 = driver.find_elements(By.CSS_SELECTOR, '.lnk-app')
print(res8)
