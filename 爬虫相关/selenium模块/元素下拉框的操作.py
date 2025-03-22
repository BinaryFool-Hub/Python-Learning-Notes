import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 下拉框功能

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://www.jq22.com/demo/shengshiliandong/')

"""根据索引值取下拉框内容, 从1开始数"""
# 选择省份
# 1. 找下拉框的标签对象<select>
province_obj = driver.find_element(By.CSS_SELECTOR, '#s_province')
# 2.实例化 select 对象, 括号内传下拉框的标签对象
province_select = Select(province_obj)
# 3.选择下拉框的内容, select_by_index --> 根据索引值取下拉框内容, 从1开始数
province_select.select_by_index(10)
time.sleep(1)

"""根据标签的 value 属性值取值"""
# 选择地级市
city_obj = driver.find_element(By.CSS_SELECTOR, '#s_city')
city_select = Select(city_obj)
# 选择下拉框的内容, select_by_value --> 根据标签的 value 属性值取值
city_select.select_by_value('黑河市')
time.sleep(1)

"""根据标签的文本取值"""
# 选择县级市
county_obj = driver.find_element(By.CSS_SELECTOR, '#s_county')
county_select = Select(county_obj)
# 选择下拉框的内容, select_by_visible_text --> 根据标签的文本取值
county_select.select_by_visible_text('北安市')

input()
