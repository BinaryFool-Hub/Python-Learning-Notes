from selenium.webdriver.chrome.options import Options  # 谷歌浏览器选项功能
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path='drive/chromedriver.exe')

"""添加无头模式"""
chrome_option = Options()  # 实例化谷歌浏览器配置对象
chrome_option.add_argument('--headless')  # 添加无头配置
#
driver = webdriver.Chrome(service=service, options=chrome_option)  # options添加配置
driver.get('https://www.baidu.com/')
driver.implicitly_wait(10)
print(driver.page_source)

input()

"""
看不见的，在后台运行
selenium的无头模式一般用于项目写完后添加, 因为写项目我们需要看到浏览器运行效果
优点: 
    相对于有界面的浏览器运行更加快
    
    
如果操作必须借助浏览器执行, 那么不能使用无头模式
"""
