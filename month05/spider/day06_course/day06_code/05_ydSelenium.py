from selenium import webdriver
import time

# 设置无界面
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 1.打开浏览器,进入翻译页
driver = webdriver.Chrome(options=options)
driver.get(url='http://fanyi.youdao.com/')
# 2.输入翻译的单词
word = input('请输入翻译的单词:')
driver.find_element_by_xpath('//*[@id="inputOriginal"]').send_keys(word)
# 3.获取翻译的结果
time.sleep(1)
result = driver.find_element_by_xpath('//*[@id="transTarget"]/p/span').text

print(result)

















