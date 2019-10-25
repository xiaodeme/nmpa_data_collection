# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 0011 16:14
# @Author  : xiaodeme
# @FileName: proxy_ip.py
# @Software: PyCharm
# @Blog    ：http://www.xiaodeme.cn

import time
import requests




test_url = 'http://mobile.cfda.gov.cn/datasearch/QueryList?pageIndex=1&pageSize=10&tableId=26'
timeout = 60

def test_proxy(proxy):
    try:
        proxies = {
            'https': 'http://' + proxy
        }
        start_time = time.time()
        requests.get(test_url, timeout=timeout, proxies=proxies)
        end_time = time.time()
        used_time = end_time - start_time
        print('Proxy Valid', 'Used Time:', used_time)
        return True, used_time
    except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
        print('Proxy Invalid:', proxy)
        return False, None