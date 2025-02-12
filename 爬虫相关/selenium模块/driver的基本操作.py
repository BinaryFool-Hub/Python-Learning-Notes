import time
from selenium.webdriver import Chrome  # 导入需要操作的浏览器对象
from selenium.webdriver.chrome.service import Service  # 导入浏览器内核驱动服务
from selenium.webdriver.common.by import By

"""
注意: 真实的浏览器渲染出来的数据, 和使用selenium得到的渲染数据可能不会一样<数据, 标签结构>
一切以代码获取的数据为准
找到的元素还可以赋值或者再进行子级操作
"""

# 实例化一个浏览器
service_obj = Service(executable_path='drive/chromedriver.exe')  # 指定浏览器操作驱动，实例化服务对象
driver = Chrome(service=service_obj)  # 传入浏览器实例服务化对象，实例化一个浏览器

# 隐式等待: 括号里面设置的是等待时间, 单位/秒;
# 会等待页面渲染, 如果页面在等待时间之前就渲染完了, 那么不会死等;  是一种智能化等待
# 网页加载6s  4s(不会在等待)，元素寻找也是，超过时间找不到就会报错
driver.implicitly_wait(10)  # 在一个py中只需要设置一次, 其他页面都遵循这个规则

# 访问页面操作
driver.get('https://www.baidu.com/')

# 截图操作
# 整个浏览器截图
driver.save_screenshot('img/baidu.png')
# 指定元素截图
driver.find_element(By.CSS_SELECTOR, '.s_form_wrapper.soutu-env-nomac.soutu-env-index').screenshot('img/元素截图.png')

# 获取浏览器渲染以后的数据
print(driver.page_source)

# 获取页面请求以后的cookies, 常用于模拟登录后获取登录的cookies片段
print(driver.get_cookies())

print(driver.current_url)  # 查看当前页面的url地址

# 返回字典 {‘width’: 宽度, ‘height’: 高度}
print(driver.get_window_size())

driver.minimize_window()  # 最小化浏览器

time.sleep(3)

driver.maximize_window()  # 最大化浏览器

""""""
# 访问新的网页
driver.get('https://news.baidu.com/')

# 死等，为了更好的展示
time.sleep(3)

# 后退页面
driver.back()

time.sleep(2)

# 前进页面
driver.forward()

time.sleep(2)

# 刷新当前的界面
driver.refresh()

time.sleep(2)

# driver.close()  # 关闭当前句柄的标签页
driver.quit()  # 退出浏览器，所有标签页和内存都进行释放
