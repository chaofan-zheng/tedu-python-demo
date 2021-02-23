"""
使用selenium打开浏览器,进入百度的搜索页面
"""
# 导入selenium的webdriver接口
from selenium import webdriver

# 1.打开浏览器 - 创建浏览器对象
driver = webdriver.Chrome()
# 浏览器窗口最大化
driver.maximize_window()
# 2.在地址栏输入 百度的URL地址
driver.get(url='http://www.baidu.com/')
# 3.page_source属性：获取HTML结构源码
html = driver.page_source
# quit(): 关闭浏览器
driver.quit()









































