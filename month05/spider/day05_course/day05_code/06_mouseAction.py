"""
selenium操控鼠标
"""
from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains

# 1.打开浏览器,输入百度URL地址
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='http://www.baidu.com/')
# 2.把鼠标移动到 设置 节点
set_node = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(set_node).perform()
# 3.找到 高级搜索 节点,并点击
driver.find_element_by_link_text('高级搜索').click()


























