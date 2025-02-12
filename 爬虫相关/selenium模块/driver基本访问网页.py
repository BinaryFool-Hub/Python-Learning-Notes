from selenium.webdriver import Chrome  # 导入需要操作的浏览器对象
from selenium.webdriver.chrome.service import Service  # 导入浏览器内核驱动服务

# 实例化一个浏览器
service_obj = Service(executable_path='drive/chromedriver.exe')  # 指定浏览器操作驱动，实例化服务对象
driver = Chrome(service=service_obj)  # 传入浏览器实例服务化对象，实例化一个浏览器

# 访问页面操作
driver.get('https://www.baidu.com')

print(driver)
