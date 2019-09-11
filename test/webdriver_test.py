# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 0009 17:46
# @Author  : xiaodeme
# @FileName: webdriver_test.py
# @Software: PyCharm
# @Blog    ：http://www.xiaodeme.cn
from selenium import webdriver  # 启动浏览器需要用到

url = 'http://app1.sfda.gov.cn/datasearchcnda/face3/search.jsp?tableId=26&curstart=1'


# option = webdriver.ChromeOptions()
# option.add_argument('headless')  # 静默模式
# 打开chrome浏览器
driver = webdriver.Chrome()
driver.get(url)
print(driver.page_source)
driver.quit()


# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# browser = webdriver.Chrome(chrome_options=option)
#
#
# browser = webdriver.Chrome()
# browser.get(url)
# data = browser.page_source
# print(data)
# browser.close()

# option = webdriver.ChromeOptions()
# option.add_argument("headless")
# browser = webdriver.Chrome(chrome_options=option)
# url = 'http://app1.sfda.gov.cn/datasearchcnda/face3/search.jsp?tableId=26&curstart=1'
# print(url)
# browser.get(url)  # Load page
# #获得网页数据
# data = browser.page_source
# print(data)