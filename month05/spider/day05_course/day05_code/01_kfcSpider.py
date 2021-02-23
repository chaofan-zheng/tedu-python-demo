"""
肯德基门店信息抓取 - POST请求
"""
import requests
import time
import random
from fake_useragent import UserAgent

class KfcSpider:
    def __init__(self):
        # F12抓包抓到的URL地址
        self.post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
        self.city = input('请输入城市名称：')

    def get_html(self, data):
        """请求功能函数"""
        headers = {'User-Agent':UserAgent().random}
        html = requests.post(url=self.post_url, data=data, headers=headers).json()

        return html

    def get_total_page(self):
        """获取所在城市的肯德基门店的总页数"""
        data = {
            'cname': self.city,
            'pid': '',
            'pageIndex': '1',
            'pageSize': '10',
        }
        html = self.get_html(data=data)
        count = html['Table'][0]['rowcount']
        total_page = count // 10 if count % 10 == 0 else count // 10 + 1

        return total_page

    def parse_html(self):
        """爬虫逻辑函数"""
        total_page = self.get_total_page()
        for page in range(1, total_page + 1):
            data = {
                'cname': self.city,
                'pid': '',
                'pageIndex': str(page),
                'pageSize': '10',
            }
            html = self.get_html(data=data)
            for one_store_dict in html['Table1']:
                item = {}
                item['rownum'] = one_store_dict['rownum']
                item['storeName'] = one_store_dict['storeName']
                item['addressDetail'] = one_store_dict['addressDetail']
                item['cityName'] = one_store_dict['cityName']
                item['provinceName'] = one_store_dict['provinceName']
                print(item)
            # 控制频率
            time.sleep(random.uniform(0, 1))

if __name__ == '__main__':
    spider = KfcSpider()
    spider.parse_html()






