# 10:33 AM, Feb 21th, 2018 @ home, Shangyu
# Pexels Crawler
# 按照关键字爬取 Pexels 网站的图片
# 使用不同的解析库测试效率
# https://www.pexels.com/

import re
import time
import requests
from bs4 import BeautifulSoup
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


# 装饰器怎么写？
def log(fn):
    print('call ' + fn.__name__)
    return fn

# 获取 res 后再用不同的库解析，避免网速的波动影响
def get_res(keyword):
    url = 'https://www.pexels.com/search/{}'.format(keyword)
    return  requests.get(url, headers=headers)

def BS_htmlparser(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    jpg_srcs = soup.select('body > div.page-wrap > div.l-container > div.photos > article > a > img')
    for jpg_src in jpg_srcs:
        jpg_src = jpg_src.get('src')
        # print(jpg_src)

def BS_lxml(res):
    soup = BeautifulSoup(res.text, 'lxml')
    jpg_srcs = soup.select('body > div.page-wrap > div.l-container > div.photos > article > a > img')
    for jpg_src in jpg_srcs:
        jpg_src = jpg_src.get('src')
        # print(jpg_src)

def Lxml_Xpath(res):
    selector = etree.HTML(res.text)
    # XPath 语法其实挺简单，img 节点中 src 后的链接，写成 /img/@src
    infos = selector.xpath('/html/body/div[1]/div[2]/div[3]/article')
    for info in infos:
        #第二个 Xpath 选取节点不需要加斜杠 /
        info = info.xpath('a[1]/img/@src')
        # print(info[0])

def re_findall(res):
    infos = re.findall(' src=\"https://(.*?)\" />', res.text)
    for info in infos:
        info = 'https://' + info
        # print(info)

def main():
    keyword = input('Please input keyword:\n')
    res = get_res(keyword)
    for crawler in [BS_htmlparser, BS_lxml, Lxml_Xpath, re_findall]:
        time_start = time.time()
        crawler(res)
        time_end = time.time()
        print(crawler.__name__, '=', time_end - time_start, '秒' , '\n')


if __name__ == '__main__':
    main()
