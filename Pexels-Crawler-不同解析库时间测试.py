# 10:33 AM, Feb 21th, 2018 @ home, Shangyu
# Pexels Crawler
# 按照关键字爬取 Pexels 网站的图片
# 使用不同的解析库测试效率
# https://www.pexels.com/

import time
import requests
from bs4 import BeautifulSoup
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def BS_htmlparser(keyword):
    url = 'https://www.pexels.com/search/{}'.format(keyword)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    jpg_srcs = soup.select('body > div.page-wrap > div.l-container > div.photos > article > a > img')
    for jpg_src in jpg_srcs:
        jpg_src = jpg_src.get('src')
        print(jpg_src)

def BS_lxml(keyword):
    url = 'https://www.pexels.com/search/{}'.format(keyword)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    jpg_srcs = soup.select('body > div.page-wrap > div.l-container > div.photos > article > a > img')
    for jpg_src in jpg_srcs:
        jpg_src = jpg_src.get('src')
        print(jpg_src)

# unfinished
def Lxml_Xpath(keyword):
    url = 'https://www.pexels.com/search/{}'.format(keyword)
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    # 郁闷，刚刚想写 Xpath ，登不上 pexels 网站了
    infos = selector.xpath('//article')
    for info in infos:
        # Xpath 应该怎么写？
        info = info.xpath('/a[1]/img') #/html/body/div[2]/div[3]/article[1]/a[1]/img
        print(info)

# unfinished
def main():
    keyword = input('Please input keyword:\n')
    # for crawler in [BS_htmlparser, BS_lxml, Lxml_Xpath, re]:
    #     time_start = time.time()
    #     crawler(keyword)
    #     time_end = time.time()
    #     print()
    crawler = Lxml_Xpath
    crawler(keyword)

if __name__ == '__main__':
    main()
