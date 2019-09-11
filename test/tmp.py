# -*- coding: utf-8 -*-
from selenium import webdriver
url = 'http://app1.sfda.gov.cn/datasearchcnda/face3/search.jsp?tableId=26&curstart=1'
option = webdriver.ChromeOptions()
# option.add_argument('--no-sandbox')

# option.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=option)
driver.get(url)
print(driver.page_source)


"""
参考 ： https://segmentfault.com/a/1190000017176131

以上代码注意需要加上，禁止在沙箱中运行
option.add_argument('--no-sandbox')
option.add_argument('--headless')

"""