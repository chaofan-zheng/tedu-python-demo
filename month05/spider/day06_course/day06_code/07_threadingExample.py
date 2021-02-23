import requests
from threading import Thread
from queue import Queue

class XxxSpider:
    def __init__(self):
        self.url = 'http://www.abc.com/page{}.html'
        self.q = Queue()

    def url_to_q(self):
        """生成所有要抓取的url地址,入队列"""
        for page in range(1, 10001):
            page_url = self.url.format(page)
            # 入队列
            self.q.put(page_url)

    def parse_html(self):
        """线程事件函数: 获取地址,请求解析数据处理"""
        while not self.q.empty():
            url = self.q.get()
            # 向url发请求,解析,数据处理
            pass

    def crawl(self):
        # url地址入队列
        self.url_to_q()
        # 创建多线程爬虫
        t_list = []
        for i in range(5):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()

if __name__ == '__main__':
    spider = XxxSpider()
    spider.crawl()

























