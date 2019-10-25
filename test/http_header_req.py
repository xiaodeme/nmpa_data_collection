# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 0022 14:06
# @Author  : xiaodeme
# @FileName: http_header_req.py
# @Software: PyCharm
# @Blog    ：http://www.xiaodeme.cn


import urllib, urllib2
def get_page_source(url):

    # headers = {'Accept': '*/*',
    #            'Accept-Language': 'en-US,en;q=0.8',
    #            'Cache-Control': 'max-age=0',
    #            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    #            'Connection': 'keep-alive',
    #            'Referer': 'http://www.baidu.com/'
    #            }

    # headers = {
    #     'Host': 'mobile.nmpa.gov.cn',
    #     'Accept': '*/*',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    #     'Connection': 'keep-alive',
    #     'tzRgz52a': 'B02zZ0hlOtmy_NO0_TUuIP7FtB14DADSVGgLzQ5EuSckL8n0PRB1ZGtqC4h8otBzc93TzxXWtLm-5zObw7DY23R_RIZGnpCRcxPG-RqPiFT-z6gI1lJUq_UehgqZzaOXVnd3BryYlpoM-unHHk7edhcvIBHaCnUU13ec0Xt..WlQMaDeUf48hBf9_0qsr484jfJAFFpqhYuxi3q0FjcDRLsepX2NyV9Yc-xlrzFQ5f6x3Rf5qRjkWC3UR-v-gAKksqxBuz8wHzte7sRKbZri4YzTMRGOUJE85we3cufkP1wQFGYSAqRKQntHHe2cN4-6-7fJJu4lZoUW-RChHsfcaSniZKZL8sWL9Yr0ERJhsENe7nmO5VIJa-pq8Ss8d3XxslsjGeFXOqrytY9qaHDULpDld0XejcpkARxyF3kpfgGD5BlBQInHNkTJ4X3ojo6AlsPfGvQ6Lzw6Y_aIytseHmyR3B-',
    #     'Connection': 'keep-alive',
    #     'User-Agent': 'SFDANewVerison/3.0.2(iPhone;iOS13.1.2;Scale/2.00)',
    #     'Set-Cookie':'5DE826D48214568DF9A2DAF3FAB2BBD6.7; Path=/datasearch'
    #
    # }

    headers = {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Referer':'http://mobile.cfda.gov.cn/datasearch/QueryList?pageIndex=15701&pageSize=10&tableId=26&searchF=Quick%20',
        'Accept-Language':'zh-CN',
        'User-Agent': 'SFDANewVerison/3.0.2(iPhone;iOS13.1.2;Scale/2.00)',
        # 'Accept-Encoding': 'gzip, deflate',
        'Host':'mobile.cfda.gov.cn',
        'Connection':'Keep-Alive',
        'Pragma':'no-cache',
        'Cookie':'JSESSIONID=BC46F6E8AE638D7A811F466E41AD6B03.7; tuNQaYE2WCOr80T=4WHyuJN_qtAC5zmkEyuf06LqeolsfA1Iv.ZOiuVHSDostVRwGkXFjiJDmE70V13jNguQkrujTa8gZ3WmD_.ewbXD4wKMefVuuvKc7WKyIezP5pNpkDdCLPgsCvFux_g.42lymbfj6EcEvtOHrLFGb3Mjthb0AbCpI3cy4m9j3pWBHUvzdTNceWshcRi_vmmw4kry3ff.7RCFjvqE9fwcl5jC5icIXz0SBkfCbj7Q9mDYtABBszfl8PFFddwCAbOtqyICpyRy7IuM4Jq.lS1bzUBOroKzqnooRAKPi7lze0nq1Qq; tuNQaYE2WCOr80S=VjXSyiob9M7r66Wm9QNeJlV1hGKQgWQCnnW.Y0MYIw6bqP91wrEe.YEecIgm0mmR'
    }

    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    page_source = response.read()
    return page_source


url = "http://syj.beijing.gov.cn/eportal/ui?pageId=331157"
text = get_page_source(url)
print(text)