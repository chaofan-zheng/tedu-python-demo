"""
请输入要翻译的单词：tiger
翻译结果：老虎
"""
import requests
import time
from hashlib import md5
import random

class YdSpider:
    def __init__(self):
        # URL地址一定要是：F12抓包抓到的POST的地址
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            # 检查频率最高的三个：Cookie、Referer、User-Agent
            "Cookie": "OUTFOX_SEARCH_USER_ID=1391264118@10.108.160.105; OUTFOX_SEARCH_USER_ID_NCOO=2105417985.4787014; JSESSIONID=aaasSeD7PiY4G_nO8cWDx; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1612506057171",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36",
        }
        # 输入要翻译的单词
        self.word = input('请输入要翻译的单词：')

    def md5_string(self, string):
        """功能函数"""
        m = md5()
        m.update(string.encode())

        return m.hexdigest()

    def get_ts_salt_sign(self):
        """获取ts salt sign"""
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        string = "fanyideskweb" + self.word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        sign = self.md5_string(string)

        return ts, salt, sign

    def attack_yd(self):
        """逻辑函数"""
        ts, salt, sign = self.get_ts_salt_sign()
        data = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": ts,
            "bv": "6a1ac4a5cc37a3de2c535a36eda9e149",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # .json():把json格式的字符串转为python数据类型
        # .join() 等同于 json.loads('{}')
        html = requests.post(url=self.post_url,
                             data=data,
                             headers=self.headers).json()

        return html['translateResult'][0][0]['tgt']

if __name__ == '__main__':
    spider = YdSpider()
    print(spider.attack_yd())































