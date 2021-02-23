"""
将图片抓取到本地文件
"""
import requests
from fake_useragent import UserAgent

image_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.sxdaily.com.cn%2FNMediaFile%2F2017%2F0123%2FSXRB201701231529000498320535793.jpg&refer=http%3A%2F%2Fwww.sxdaily.com.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1615015262&t=b49b989cf1f8b07fc0b4b971c057bd22'
headers = { 'User-Agent':UserAgent().random }
image_html = requests.get(url=image_url, headers=headers).content

with open('girl.jpg', 'wb') as f:
    f.write(image_html)
















