#coding=gbk

import urllib2

'''
ץȡ���ݷ���
'''
def get_data(url):
    html = urllib2.urlopen(url).read()
    return html