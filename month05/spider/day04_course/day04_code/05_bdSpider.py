"""
百度翻译破解案例 - JS逆向(execjs模块)
"""
import requests
import execjs
import re

class BdSpider:
    def __init__(self):
        # url：F12抓包抓到的POST的URL地址
        self.post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.post_headers = {
            '''Accept''': '''*/*''',
            '''Accept-Encoding''': '''gzip, deflate, br''',
            '''Accept-Language''': '''zh-CN,zh;q=0.9''',
            '''Cache-Control''': '''no-cache''',
            '''Connection''': '''keep-alive''',
            '''Content-Length''': '''135''',
            '''Content-Type''': '''application/x-www-form-urlencoded; charset=UTF-8''',
            '''Cookie''': '''BIDUPSID=F29F6E28B0FBCFC1A7E211DE92583124; PSTM=1608988098; BAIDUID=F29F6E28B0FBCFC153ABCCC1188CE960:FG=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_duid=1_40d64069dbd8841dbfa1e003a7c7dd8a1611644719974; BDSFRCVID_BFESS=WauOJeC627FxfbveyBYtbHBDYpJWrfTTH6aoVfeprTJ6BRthQWFTEG0P8M8g0KubvwPHogKKBmOTHgLF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJI8oK0XJD-3fP36qR6sMJI0hU5054RB2C6yX4K8Kb7VbU3p5fnkbfJBDGJlhP5abDT85fT2KqnIsMTxylJKbl07yajK2h5h56RH-pFK0foMjMj5QlOpQT8re-FOK5OibCrqLMJdab3vOpozXpO1bUAzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqtJHKbDOVC_K3D; BDUSS=U5hRU50YVFPZmdLbnZ3QTlZYWJDdXpkZ2VRSUtDZzl3V0o4TEY1Z3d5YVhlMEJnRVFBQUFBJCQAAAAAAAAAAAEAAAADZykQv9u~2zMwOTQzNTM2NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJfuGGCX7hhge; BDUSS_BFESS=U5hRU50YVFPZmdLbnZ3QTlZYWJDdXpkZ2VRSUtDZzl3V0o4TEY1Z3d5YVhlMEJnRVFBQUFBJCQAAAAAAAAAAAEAAAADZykQv9u~2zMwOTQzNTM2NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJfuGGCX7hhge; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1610182098,1610437054,1610501127,1612504926; H_PS_PSSID=33423_33439_33273_31660_33595_33540_33590_26350; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; BA_HECTOR=8l2kag0h21052l24g91g1ps820r; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1612509484; __yjsv5_shitong=1.0_7_7b5b5c8481cf67b7c1053df9dfdc2105d925_300_1612509484292_101.30.65.196_f2e2fdf6; ab_sr=1.0.0_MGIyNDA3Mjk2NGU4NjAxZjkzYzU5YjQ4Mjg3YjJmMTFjMzRjY2E0Y2EwYWE5YTllZGE2Yjk5NmM2M2RjZmViMjUwMjIyZGJlODNhZDJkOTk0YjNkMjRiNTE0NjM4YzEx''',
            '''Host''': '''fanyi.baidu.com''',
            '''Origin''': '''https://fanyi.baidu.com''',
            '''Pragma''': '''no-cache''',
            '''Referer''': '''https://fanyi.baidu.com/''',
            '''sec-ch-ua''': '''"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"''',
            '''sec-ch-ua-mobile''': '''?0''',
            '''Sec-Fetch-Dest''': '''empty''',
            '''Sec-Fetch-Mode''': '''cors''',
            '''Sec-Fetch-Site''': '''same-origin''',
            '''User-Agent''': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36''',
            '''X-Requested-With''': '''XMLHttpRequest''',
        }
        self.word = input('请输入翻译单词：')
        # 获取gtk和token的
        self.get_url = 'https://fanyi.baidu.com/'
        self.get_headers = {
            '''Accept''': '''text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9''',
            '''Accept-Encoding''': '''gzip, deflate, br''',
            '''Accept-Language''': '''zh-CN,zh;q=0.9''',
            '''Cache-Control''': '''no-cache''',
            '''Connection''': '''keep-alive''',
            '''Cookie''': '''BIDUPSID=F29F6E28B0FBCFC1A7E211DE92583124; PSTM=1608988098; BAIDUID=F29F6E28B0FBCFC153ABCCC1188CE960:FG=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_duid=1_40d64069dbd8841dbfa1e003a7c7dd8a1611644719974; BDSFRCVID_BFESS=WauOJeC627FxfbveyBYtbHBDYpJWrfTTH6aoVfeprTJ6BRthQWFTEG0P8M8g0KubvwPHogKKBmOTHgLF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJI8oK0XJD-3fP36qR6sMJI0hU5054RB2C6yX4K8Kb7VbU3p5fnkbfJBDGJlhP5abDT85fT2KqnIsMTxylJKbl07yajK2h5h56RH-pFK0foMjMj5QlOpQT8re-FOK5OibCrqLMJdab3vOpozXpO1bUAzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqtJHKbDOVC_K3D; BDUSS=U5hRU50YVFPZmdLbnZ3QTlZYWJDdXpkZ2VRSUtDZzl3V0o4TEY1Z3d5YVhlMEJnRVFBQUFBJCQAAAAAAAAAAAEAAAADZykQv9u~2zMwOTQzNTM2NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJfuGGCX7hhge; BDUSS_BFESS=U5hRU50YVFPZmdLbnZ3QTlZYWJDdXpkZ2VRSUtDZzl3V0o4TEY1Z3d5YVhlMEJnRVFBQUFBJCQAAAAAAAAAAAEAAAADZykQv9u~2zMwOTQzNTM2NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJfuGGCX7hhge; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1610182098,1610437054,1610501127,1612504926; H_PS_PSSID=33423_33439_33273_31660_33595_33540_33590_26350; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1612514819; __yjsv5_shitong=1.0_7_7b5b5c8481cf67b7c1053df9dfdc2105d925_300_1612514819989_101.30.65.196_430628f1; ab_sr=1.0.0_NjNjMjA3YzcyNDdiMzE4Njk5MGRkNjY1ZTY2YmFiNTI4MzE2ODQ3ZDIwYjBmNGRlZWFjODgyOGFjMGY0ZTQ3ODVlM2MxNDYxMjQ2ZWYzZGFkM2EzYWFjZjYyM2RkY2Vi''',
            '''Host''': '''fanyi.baidu.com''',
            '''Pragma''': '''no-cache''',
            '''sec-ch-ua''': '''"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"''',
            '''sec-ch-ua-mobile''': '''?0''',
            '''Sec-Fetch-Dest''': '''document''',
            '''Sec-Fetch-Mode''': '''navigate''',
            '''Sec-Fetch-Site''': '''none''',
            '''Sec-Fetch-User''': '''?1''',
            '''Upgrade-Insecure-Requests''': '''1''',
            '''User-Agent''': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36''',
        }

    def get_gtk_token(self):
        """获取gtk和token"""
        html = requests.get(url=self.get_url,
                            headers=self.get_headers).text
        gtk = re.findall("window.gtk = '(.*?)'", html, re.S)[0]
        token = re.findall("token: '(.*?)'", html, re.S)[0]

        return gtk, token

    def get_sign(self):
        """获取sign"""
        gtk, token = self.get_gtk_token()
        with open('translate.js', 'r') as f:
            jscode = f.read()

        jsobj = execjs.compile(jscode)
        sign = jsobj.eval('e("{}","{}")'.format(self.word, gtk))

        return sign

    def attack_bd(self):
        """逻辑函数"""
        sign = self.get_sign()
        gtk, token = self.get_gtk_token()
        data = {
            "from": "en",
            "to": "zh",
            "query": self.word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": token,
            "domain": "common",
        }
        html = requests.post(url=self.post_url,
                             data=data,
                             headers=self.post_headers).json()

        return html['trans_result']['data'][0]['dst']

if __name__ == '__main__':
    spider = BdSpider()
    print(spider.attack_bd())








