"""
百度贴吧视频抓取
1、向帖子链接发请求,提取具体：视频的链接
2、向视频的链接发请求,将响应内容以 wb 的方式保存到本地文件
"""
import requests
from lxml import etree
from fake_useragent import UserAgent

# 1.提取帖子中视频的链接
url = 'https://tieba.baidu.com/p/7216913650'
headers = {'User-Agent' : UserAgent().random}
html = requests.get(url=url, headers=headers).text
eobj = etree.HTML(html)
src_list = eobj.xpath('//embed/@data-video')
if src_list:
    video_url = src_list[0]
    # 向视频链接发请求,并将其保存到本地即可
    video_html = requests.get(url=video_url, headers=headers).content
    with open('赵丽颖.mp4', 'wb') as f:
        f.write(video_html)
else:
    print('提取视频链接失败')










































