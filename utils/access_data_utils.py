#coding=utf-8
import urllib2
import ConfigParser


# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")



'''
抓取数据方法
'''
def get_data(url):
    try:
        timeout = int(cf.get("default_config", "timeout"))
        f = urllib2.urlopen(url, timeout=timeout)
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