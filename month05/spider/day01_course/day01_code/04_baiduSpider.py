"""
请输入关键字：赵丽颖
最终保存 赵丽颖.html 到本地文件
"""
import requests

# 1.拼接URL地址
keyword = input('关键字:')
url = 'http://tieba.baidu.com/s?wd={}'.format(keyword)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
}

# 2.发请求获取响应内容(右键->查看网页源代码)
html = requests.get(url=url, headers=headers).content.decode('utf-8')

# 3.保存文件
filename = '{}.html'.format(keyword)
with open(filename, 'w') as f:
    f.write(html)




















