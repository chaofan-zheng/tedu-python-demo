"""
https://www.guazi.com/nc/buy/o1/#bread
第1页：o1
第2页：o2
第n页：on
"""
url = 'https://www.guazi.com/nc/buy/o{}/#bread'
for page in range(1, 51):
    page_url = url.format(page)
    print(page_url)


# https://www.baidu.com/s?wd=张靓颖&pn={}
# 第1页：pn=0
# 第2页：pn=10
# 第n页：(n-1) * 10
url = 'https://www.baidu.com/s?wd=张靓颖&pn={}'
for i in range(100):
    page_url = url.format( i * 10 )
    print(page_url)
















