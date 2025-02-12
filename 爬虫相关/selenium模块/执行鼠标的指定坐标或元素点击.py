import time

from selenium.webdriver import ActionChains  # 鼠标动作链对象
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)

# context_click() 右键点击
# click() 左键点击

driver.get('https://www.baidu.com')

"""
move_by_offset：移动到相对于电脑的指定坐标
"""
# 不同电脑 分辨率 不一样要手动修正
# 需要自行调整
# ActionChains(driver).move_by_offset(500, 200).context_click().perform()

"""移动到指定元素"""
# eme = driver.find_element(By.ID, 'su')
# ActionChains(driver).move_to_element(eme).context_click().perform()


"""
将鼠标移动指定元素的偏移量。偏移量为
相对于元件的视线中心点。

# selenium4.0往上的方法ActionChains(driver).move_to_element_with_offset(img_obj,x,y).click().perform()
# 是以中心为原点进行计算点击（宽度和高度除以2即可视为左上角坐标开始）
"""
eme = driver.find_element(By.ID, 'su')
ActionChains(driver).move_to_element_with_offset(eme, 10, 10).context_click().perform()

time.sleep(3)
