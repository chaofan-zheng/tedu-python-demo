"""
根据文件 log.txt完成
文件特征: 每段之间有空行
         每段首个单词是设备名称

要求： 设计程序完成，输入一个设备名称
得到该设备的 address is 值

思路：* 先根据用户输入提取出设备描述段落
　　　* 再从该段中取出目标字符串
"""
import re

# 通过输入提取出设备描述段落 （生成器）
def get_info():
    file = open("log.txt")
    # 每次while循环获取一段内容
    while True:
        info = ""
        for line in file:
            # line如果是\n说明是空行
            if line == '\n':
                break
            info += line
        # 文件结束
        if info:
            yield info  # 提供一段内容
        else:
            file.close()
            return


# 从设备描述段中匹配出目标 （最终目的）
def main(port):
    """
    :param port:  设备名称
    :return: 匹配到的内容
    """
    # 每次获取一段内容
    for info in get_info():
        #　提取首单词
        key = re.match(r"\S+",info)
        if port == key.group():
            #　开始匹配ａｄｄｒｅｓｓ
            pattern=r"([0-9a-f]{4}\.){2}[0-9a-f]{4}"
            result = re.search(pattern,info)
            return result.group()


if __name__ == '__main__':
    port = input("请输入设备名：")
    print("获取值：",main(port))