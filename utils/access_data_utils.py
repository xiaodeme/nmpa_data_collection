#coding=gbk

import urllib2

'''
抓取数据方法
'''
def get_data(url):
    html = urllib2.urlopen(url).read()
    return html