"""
利用requests模块抓取民政部数据网站
"""
import requests
from lxml import etree
from fake_useragent import UserAgent
import re

class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers = {'User-Agent':UserAgent().random}

    def get_html(self, url):
        """功能函数"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def xfunc(self, html, x):
        """功能函数"""
        eobj = etree.HTML(html)
        r_list = eobj.xpath(x)

        return r_list

    def first_page(self):
        """爬虫逻辑函数"""
        first_html = self.get_html(url=self.url)
        # 页面中的节点结构和响应内容不完全一致
        first_x = '//table/tr[1]/td[2]/a[@class="artitlelist"]/@href'
        href_list = self.xfunc(first_html, first_x)
        if href_list:
            # 开始发请求具体提取数据
            second_url = 'http://www.mca.gov.cn' + href_list[0]
            self.get_data(second_url)
        else:
            print('最新月份链接提取失败')

    def get_data(self, second_url):
        """获取真实数据"""
        # 从second_html中提取跳转之后的真实链接
        second_html = self.get_html(url=second_url)
        regex = 'window.location.href="(.*?)"'
        href_list = re.findall(regex, second_html, re.S)
        if href_list:
            # 开始提取具体数据
            real_url = href_list[0]
            self.get_really_data(real_url)
        else:
            print('提取真实链接失败')

    def get_really_data(self, real_url):
        """提取具体数据的函数"""
        real_html = self.get_html(url=real_url)
        second_x = '//tr[@height="19"]'
        tr_list = self.xfunc(real_html, second_x)
        for tr in tr_list:
            item = {}
            item['title'] = tr.xpath('./td[3]/text()')[0]
            item['code'] = tr.xpath('./td[2]/text() | ./td[2]/span/text()')[0]
            print(item)


if __name__ == '__main__':
    spider = MzbSpider()
    spider.first_page()










































