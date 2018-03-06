# Crawler DifferentLib TimeTest
测试不同库解析HTML页面的速度差异

### Mar 6th, 2018, 8:15PM @HDU_Wireless

## 代码目的

测试以下几个不同方法解析 html 页面的速度

* BeautifulSoup + 'html.parser' + select
* BeautifulSoup + 'lxml' + select
* Lxml + etree + XPath
* re + findall

## 测试结果

如图所示

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/%E4%B8%8D%E5%90%8C%E8%A7%A3%E6%9E%90%E5%BA%93%E6%97%B6%E9%97%B4%E6%B5%8B%E8%AF%95.PNG?raw=true)

## 结果分析

为了避免网速波动的影响，整个程序只请求了一次 request ，然后用不同的库解析同一个 html 页面。  

从测试结果可以看出，BeautifulSoup 配合 Python 内置的 html.parser 速度最慢，换成 lxml 变快了一些。  

第二块的是 Lxml 库的 etree 配合 XPath 语法。  

最快的是采用正则表达式，re模块的表达式得凑，很少能一次猜对，这需要一定经验和技巧
