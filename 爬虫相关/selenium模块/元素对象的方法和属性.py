from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)

"""
find_element 单个对象
注意: 如果用 find_elements 取对象, 返回的是列表, 列表类型是不支持selenium属性的, 会报错 [对象,对象,对象]
解决: 遍历列表中的标签对象, 调用selenium属性或者方法
"""

driver.get('https://www.douban.com/')

"""
text    是标签对象的属性
        获取标签包含的文本内容
        支持链式调用
"""
res1 = driver.find_element(By.CSS_SELECTOR, '.lnk-app').text
print(res1)

"""
get_attribute('属性名')
    方法, 根据属性名获取其属性值
    支持链式调用
"""
res2 = driver.find_element(By.CSS_SELECTOR, '.lnk-app').get_attribute('href')
print(res2)

"""
send_keys('输入字符')
    向输入框中输入字符串
    支持链式调用
"""
res3 = driver.find_element(By.NAME, 'q')
res3.send_keys('肖申克的救赎')
print(res3)

"""
click()   指定标签的点击操作, 需要标签具有点击事件
"""

driver.find_element(By.CSS_SELECTOR, '.bn>input').click()

"""
rect()  包含元素大小和位置的字典。
"""
half_width = driver.find_element(By.CSS_SELECTOR, '.bn>input').rect['width']
half_height = driver.find_element(By.CSS_SELECTOR, '.bn>input').rect['height']

input()  # 阻塞，等待用户回车确定
