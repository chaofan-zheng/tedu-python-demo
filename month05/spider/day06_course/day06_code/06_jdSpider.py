from selenium import webdriver
import time

class JdSpider:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url='https://www.jd.com/')
        self.driver.find_element_by_xpath('//*[@id="key"]').send_keys("爬虫书")
        self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)

    def get_one_page(self):
        """获取商品数据"""
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        # 一定给页面元素的加载预留时间
        time.sleep(2)
        # 提取数据
        li_list = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            print(li.text)
            print('*' * 50)

    def crawl(self):
        while True:
            self.get_one_page()
            if self.driver.page_source.find("pn-next disabled") == -1:
                self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
                time.sleep(1)
            else:
                self.driver.quit()
                break

if __name__ == '__main__':
    spider = JdSpider()
    spider.crawl()























