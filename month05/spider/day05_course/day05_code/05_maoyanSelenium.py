"""
selenium抓取猫眼电影top100
"""
from selenium import webdriver

# 设置无头模式(无界面模式)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(url='https://maoyan.com/board/4')

def get_one_page():
    """获取1页电影数据的函数"""
    dd_list = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    for dd in dd_list:
        item = {}
        # text属性：获取当前节点以及子节点和后代节点的文本内容
        info_list = dd.text.split('\n')
        item['rank'] = info_list[0].strip()
        item['title'] = info_list[1].strip()
        item['star'] = info_list[2].strip()
        item['time'] = info_list[3].strip()
        item['score'] = info_list[4].strip()
        print(item)

# 1. 获取10页的电影数据
# 如果可以的话,能否让程序自己判断是否为最后一页
while True:
    get_one_page()
    try:
        # find_element : 找不到节点会抛出异常NoSuchElementException
        driver.find_element_by_link_text('下一页').click()
    except Exception as e:
        driver.quit()
        break




















