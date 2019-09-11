# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 0010 15:34
# @Author  : xiaodeme
# @FileName: http_req.py
# @Software: PyCharm
# @Blog    ：http://www.xiaodeme.cn
from selenium import webdriver


# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
browser = webdriver.Chrome(chrome_options=options)
url = "http://mobile.cfda.gov.cn/datasearch/QueryList?pageIndex=1&pageSize=10&tableId=26"
browser.get(url)
# browser.quit()
