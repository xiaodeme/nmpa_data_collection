#coding=utf-8
import urllib2
import socket
class MyException(Exception):
    pass


'''
抓取数据方法
'''
def get_data(url):
    # html = urllib2.urlopen(url).read()
    # return html

    try:
        f = urllib2.urlopen(url, timeout=2)
        return f.read()
    except urllib2.URLError, e:
        raise e


def get_test_timeout():
    try:
        url = 'http://localhost:8081/?name=2000'
        data = get_data(url)
        print data
    except urllib2.URLError, e:
        raise e

if __name__ == "__main__":
    try:
        url = 'http://localhost:8081/?name=4000'
        data = get_data(url)
        print data
    except urllib2.URLError, e:
        print e
        print 1111