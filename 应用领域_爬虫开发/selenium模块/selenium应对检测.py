from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path='drive/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 此设置需要加在紧跟实例化浏览器对象的后面
"""判断navigator.webdriver是否为false，selenium是自动化程序，默认为true"""
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})

driver.get('https://antispider1.scrape.center')

driver.implicitly_wait(10)
input()
