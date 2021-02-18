"""
向京东官网发请求,拿到响应内容
"""
import requests

# get(): 获取响应对象
resp = requests.get(url='https://www.jd.com/')
# text属性：获取响应内容-字符串(右键->查看网页源代码)
html = resp.text
# content属性：获取响应内容-bytes(抓取图片、文件、音频、视频...)
html = resp.content
# status_code属性：获取HTTP响应码
code = resp.status_code
# url属性：返回实际数据的URL地址
url = resp.url
print(url)















