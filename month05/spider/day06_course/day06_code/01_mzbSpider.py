"""
切换句柄 - 民政部最新行政区划代码数据抓取
"""
import sys

from selenium import webdriver
import time
import redis
from hashlib import md5

class MzbSpider:
    def __init__(self):
        # 设置无界面
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)

        self.driver.get(url='http://www.mca.gov.cn/article/sj/xzqh/2020/')
        self.r = redis.Redis(host='localhost',port=6379,db=0)

    def md5_href(self, href):
        """md5加密的功能函数"""
        m = md5()
        m.update(href.encode())

        return m.hexdigest()

    def parse_html(self):
        """解析提取数据"""
        new_month_a = self.driver.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[1]/td[2]/a')
        # 生成指纹
        href = new_month_a.get_attribute('href')
        finger = self.md5_href(href)
        if self.r.sadd('mzb:spiders', finger) == 1:
            new_month_a.click()
            time.sleep(3)
            # 切换句柄
            li = self.driver.window_handles
            self.driver.switch_to.window(li[1])
            # 开始提取数据(单独写了个函数提取数据而已)
            self.get_data()
        else:
            sys.exit('更新完成')

    def get_data(self):
        """提取具体数据"""
        tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            item = {}
            li = tr.text.split()
            item['code'] = li[0]
            item['name'] = li[1]
            print(item)
        # 关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.parse_html()





































