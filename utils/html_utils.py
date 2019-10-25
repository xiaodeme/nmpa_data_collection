# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 0009 19:53
# @Author  : xiaodeme
# @FileName: html_utils.py
# @Software: PyCharm
# @Blog    ：http://www.xiaodeme.cn
from lxml import html
from utils import  comm_utils
import  ConfigParser
from selenium import webdriver

# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")


def get_curr_nmpa_total_count(data_type):
    data_list_url = cf.get("html_access_url", "data_list_url")
    data_list_url = data_list_url.format(data_type, 1)
    if comm_utils.is_windows():
        browser = webdriver.Chrome()
        browser.get(data_list_url)
        data_list_data = browser.page_source
    else:
        option = webdriver.ChromeOptions()
        option.add_argument('--no-sandbox')
        option.add_argument('--headless')

        browser = webdriver.Chrome(chrome_options=option)
        browser.get(data_list_url)
        data_list_data = browser.page_source


    #文本解析(第 1 页 共10785页 共161766条)
    selector = html.fromstring(data_list_data)
    data_list_data = selector.xpath('/html/body/table[4]/tbody/tr/td[1]')
    data_list_data =  data_list_data[0].text

    return get_info(data_list_data)



def get_info(text):
    # text = unicode(text, "gbk")
    # print text

    a = text.find(u"共")
    b = text.rfind(u"页")

    c = text.rfind(u"共")
    d = text.rfind(u"条")

    total_page_count  = text[a + 1:b]
    total_count =  text[c + 1:d]

    # print("当前数据总量:%s,共有:%s页" % (total_count,total_page_count))

    # print total_count
    # print total_page_count
    return total_page_count,total_count


if __name__ == '__main__':
    total_page_count, total_count = get_curr_nmpa_total_count(26)
    print total_count
    print total_page_count

