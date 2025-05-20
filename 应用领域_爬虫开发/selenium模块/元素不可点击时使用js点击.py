from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

service_obj = Service(executable_path='drive/chromedriver.exe')
driver = Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get('https://www.baidu.com')
driver.find_element(By.ID, 'kw').send_keys('电脑')
driver.find_element(By.ID, 'su').click()

"""当元素不可点击时"""

next_obj = driver.find_element(By.CSS_SELECTOR, 'a[class="n"]')
# js 点击; 不需要看到页面翻页标签也可以点击
# next_obj 会被传入到 arguments[0], 然后 click()
driver.execute_script('arguments[0].click();', next_obj)  # 利用js点击标签对象

input()
