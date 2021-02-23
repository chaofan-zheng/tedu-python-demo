# -*- coding: utf-8 -*-
import scrapy
import requests
from ..items import TencentItem
import json

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1608216394591&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1608216394591&postId={}&language=zh-cn'
    keyword = input('请输入关键字:')
    # 某个类别下第一页的url地址
    start_urls = [one_url.format(keyword, 1)]

    def get_total(self):
        """获取某个类别下的总页数"""
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
        html = requests.get(url=self.one_url.format(self.keyword, 1), headers=headers).json()
        count = html['Data']['Count']
        total = count // 10 if count % 10 == 0 else count // 10 + 1

        return total

    def parse(self, response):
        """生成所有页的一级页面的url地址,交给调度器入队列"""
        total = self.get_total()
        for index in range(1, total + 1):
            page_url  = self.one_url.format(self.keyword, index)
            # dont_filter: 让交给调度器的此请求不参与去重
            yield scrapy.Request(url=page_url, dont_filter=True, callback=self.parse_one_page)

    def parse_one_page(self, response):
        """一级页面解析: 提取postId的值,用于拼接职位详情页的地址"""
        one_html = json.loads(response.text)
        for one_job_dict in one_html['Data']['Posts']:
            post_id = one_job_dict['PostId']
            job_info_url = self.two_url.format(post_id)
            # 把详情页的Url地址交给调度器入队列
            yield scrapy.Request(url=job_info_url, callback=self.parse_two_page)

    def parse_two_page(self, response):
        # 获取响应内容,并转为python数据类型
        html = json.loads(response.text)
        # 提取具体数据
        item = TencentItem()
        item['job_name'] = html['Data']['RecruitPostName']
        item['job_type'] = html['Data']['CategoryName']
        item['job_duty'] = html['Data']['Responsibility']
        item['job_require'] = html['Data']['Requirement']
        item['job_add'] = html['Data']['LocationName']
        item['job_time'] = html['Data']['LastUpdateTime']

        # 至此,一条完整数据提取完成,交给项目管道去处理
        yield item




