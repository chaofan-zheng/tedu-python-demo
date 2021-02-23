"""
selenium切换iframe子页面
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://music.163.com/#/discover/toplist')
# 1.切换iframe
driver.switch_to.frame('contentFrame')
# 2.提取歌曲数据
tr_list = driver.find_elements_by_xpath('//table/tbody/tr')
for tr in tr_list:
    item = {}
    item['rank'] = tr.find_element_by_xpath('.//span[@class="num"]').text
    item['title'] = tr.find_element_by_xpath('.//span[@class="txt"]/a/b').get_attribute('title').replace('\xa0', ' ')
    item['time'] = tr.find_element_by_class_name("u-dur ").text
    item['star'] = tr.find_element_by_xpath('.//div[@class="text"]/span').get_attribute('title')
    print(item)

# 关闭浏览器
driver.quit()













