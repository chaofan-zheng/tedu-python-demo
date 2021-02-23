from selenium import webdriver

# 1. 打开浏览器,输入百度URL地址
driver = webdriver.Chrome()
driver.get(url='http://www.baidu.com/')
# 2. 找到搜索框节点,并发送关键字：高圆圆
node = driver.find_element_by_xpath('//*[@id="kw"]')
node.send_keys('高圆圆')
# 3. 找到 百度一下 按钮,并点击确认
driver.find_element_by_xpath('//*[@id="su"]').click()


















