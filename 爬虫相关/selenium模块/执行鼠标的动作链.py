import time

from selenium.webdriver import ActionChains  # 鼠标动作链对象
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.switch_to.frame(0)  # 这个网址是嵌套网页 所以需要切换

# 找到可以拖动的标签
drag = driver.find_element(By.CSS_SELECTOR, '#draggable')

# 找到需要放置标签的位置
drop = driver.find_element(By.CSS_SELECTOR, '#droppable')

"""
click_and_hold：按住元素上的鼠标左键
move_by_offset：将鼠标移动到与当前鼠标位置偏移的位置
"""
# 鼠标动作链滑动
action = ActionChains(driver)
action.click_and_hold(drag)  # 鼠标点击指定的标签对象保持点击的状态, 按住不动
action.move_by_offset(xoffset=30, yoffset=300)  # 进行距离移动
# 提交结束
action.perform()

time.sleep(5)

"""
drag_and_drop：
按住源元素上的鼠标左键，然后移动到目标元素并释放鼠标按钮。
"""
# 实例化一个动作链对象, 括号内部需要传递当前driver浏览器对象
action = ActionChains(driver)
# 定义一个鼠标动作, 但是动作到目前为止还没有执行
action.drag_and_drop(drag, drop)
# perform() 执行鼠标动作链 提交
action.perform()

input()
