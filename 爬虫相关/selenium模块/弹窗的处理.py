import time
from selenium.webdriver import ActionChains  # 鼠标动作链对象
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.switch_to.frame(0)  # 这个网址是嵌套网页 所以需要切换

# 找到可以拖动的标签
drag = driver.find_element(By.CSS_SELECTOR, '#draggable')

# 找到需要放置标签的位置
drop = driver.find_element(By.CSS_SELECTOR, '#droppable')

"""鼠标动作链操作"""
# 实例化一个动作链对象, 括号内部需要传递当前driver浏览器对象
action = ActionChains(driver)
# 定义一个鼠标动作, 但是动作到目前为止还没有执行
action.drag_and_drop(drag, drop)
# perform() 执行鼠标动作链 提交
action.perform()

time.sleep(1)
"""处理弹窗"""
obj = driver.switch_to.alert  # 切换到弹窗
# 取消
# obj.dismiss()
# 确定
obj.accept()

input()
