import requests
import re
from lxml import etree

for m in range(1,50):
    url = "https://s.weibo.com/weibo/%25E4%25B8%25AD%25E5%258C%25BB?topnav=1&wvr=6&b=1&page="
    url1 = url+str(m)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"}
    r = requests.get(url1, headers=headers)
    r.encoding = 'utf-8'
    html = etree.HTML(r.text)
    s1 = '//*[@id="pl_feedlist_index"]/div[1]/div['
    s2 = ']/div/div[1]/div[2]/p[1]/text()'
    for n in range(2, 23):
        s3 = str(s1 + str(n) + s2)
        xy = html.xpath(s3)
        file = open("D:/lianxi/ciyun/xx.txt", 'a', encoding="utf-8")
        if len(xy):
            for x in xy:
                print(x)
                file.write(x)
            file.close()
