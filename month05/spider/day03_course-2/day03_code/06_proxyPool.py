"""
建立代理IP池 - 开放代理
"""
import requests
from fake_useragent import UserAgent

class ProxyPool:
    def __init__(self):
        self.api_url = 'http://dps.kdlapi.com/api/getdps/?orderid=941243088971329&num=20&pt=1&sep=1'
        self.test_url = 'http://httpbin.org/get'
        self.headers = {'User-Agent':UserAgent().random}

    def get_proxy(self):
        """获取代理IP"""
        html = requests.get(url=self.api_url,
                            headers=self.headers).text
        proxy_list = html.split('\r\n')
        for proxy in proxy_list:
            # proxy: 1.1.1.1:8888
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        """测试1个代理IP是否可用"""
        proxies = {
            'http' : 'http://309435365:szayclhp@{}'.format(proxy),
            'https': 'https://309435365:szayclhp@{}'.format(proxy)
        }
        try:
            resp = requests.get(url=self.test_url,
                                proxies=proxies,
                                headers=self.headers,
                                timeout=3)
            print(proxy, '\033[31m可用\033[0m')
        except Exception as e:
            print(proxy, '不可用')

if __name__ == '__main__':
    spider = ProxyPool()
    spider.get_proxy()






























