# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 0010 15:34
# @Author  : xiaodeme
# @FileName: http_req.py
# @Software: PyCharm
# @Blog    ：http://www.xiaodeme.cn
# -*-coding:utf-8-*-

import urllib2
import random

url = "http://mobile.cfda.gov.cn/datasearch/QueryList?pageIndex=1&pageSize=10&tableId=26"

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"

    ]


def get_content(url, headers):
    '''
    @获取403禁止访问的网页
    '''
    randdom_header = random.choice(headers)

    req = urllib2.Request(url)
    req.add_header("User-Agent", randdom_header)
    req.add_header("Host", "mobile.cfda.gov.cn")
    req.add_header("Referer", "http://mobile.cfda.gov.cn/datasearch/QueryList?pageIndex=1&pageSize=1&tableId=26")
    req.add_header("GET", url)

    content = urllib2.urlopen(req).read()
    return content


print get_content(url, my_headers)
