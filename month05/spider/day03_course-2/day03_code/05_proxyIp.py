"""
免费代理IP测试
向测试网站发请求,打印响应内容,查看origin对应的IP是什么
"""
import requests
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers = { 'User-Agent' : UserAgent().random }
proxies = {
    'http' : 'http://27.43.191.107:9999',
    'https': 'https://27.43.191.107:9999'
}
html=requests.get(url=url,proxies=proxies,headers=headers).text
# 确认：html中的IP是自己真实IP还是proxies的IP
print(html)












