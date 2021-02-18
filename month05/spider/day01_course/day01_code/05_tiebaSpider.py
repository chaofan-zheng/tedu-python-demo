"""
贴吧名：迪丽热巴吧
起始页：2
终止页：6
迪丽热巴吧_第2页.html  迪丽热巴吧_第3页.html .......

思路：
    1、确认数据来源：右键查看网页源代码,搜索关键字
    2、响应内容中存在：观察URL地址规律
    3、写程序
"""
import requests
import time
import random

class TieBaSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

    def get_html(self, url):
        """请求函数"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def parse_html(self):
        """解析函数"""
        pass

    def save_html(self, filename, html):
        """数据处理函数"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def crawl(self):
        """爬虫逻辑函数"""
        name = input('贴吧名：')
        start = int(input('起始页：'))
        end = int(input('终止页：'))
        for page in range(start, end + 1):
            # 脑海中闪现出self.url中有几个{} ？？？？？
            pn = (page - 1) * 50
            page_url = self.url.format(name, pn)
            page_html = self.get_html(url=page_url)
            # 迪丽热巴吧_第2页.html
            filename = '{}_第{}页.html'.format(name, page)
            self.save_html(filename, page_html)
            print(filename, '抓取成功')
            # 控制数据抓取的频率
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider = TieBaSpider()
    spider.crawl()
























