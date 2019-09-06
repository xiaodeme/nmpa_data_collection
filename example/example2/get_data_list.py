#coding=utf-8
import urllib2
import time
import json
import os
from selenium import webdriver

from utils import file_utils
from utils import etc_utils

import logging
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import Queue
import threading
import ConfigParser
import traceback

# 初始化队列，用于保存待抓取页码值
temp_queue = Queue.Queue()

#获取配置信息
dataTypeConfig = etc_utils.DataTypeConfig(26,"../etc/example2_get_type.cfg")
data_list_url = dataTypeConfig.get_data_list_url()
data_type =  int(dataTypeConfig.get_data_type())
total_count = int(dataTypeConfig.get_total_count())
total_page_count = int(dataTypeConfig.get_total_page_count())
save_root_path =   dataTypeConfig.get_save_root_path()
thread_count =     int(dataTypeConfig.get_thread_count())

#数据保存路径
DATA_LIST_PATH = save_root_path +  "/data_list/"
file_utils.mkdir_path(DATA_LIST_PATH)

#日志保存路径
LOG_PATH =    save_root_path + "/logs/"
file_utils.mkdir_path(LOG_PATH)

'''
初始化数据，更多信息需分析nmpa官网
'''
def init_data():

    # 日志配置
    log_name = LOG_PATH + "/get_data_list.log"
    file_utils.logConfig(log_name)

    #数据获取总量初始化
    #用于程序中断后重新启动，其初始页码应该等于当前已经获取最大页码数+1
    startIndex = file_utils.get_curr_max_pageno(DATA_LIST_PATH) + 1
    endIndex = total_page_count + 1

    for x in range(startIndex,endIndex):
        temp_queue.put(x)
    info = "加入队列总页数：" + str(temp_queue.qsize())
    logging.info(info)
    print(info)


'''
从cfda数据库抓取数据
@threadName初始化线程名称
'''
def get_data_list(threadName):
        try:
            while not temp_queue.empty():
                curstart = temp_queue.get()
                info = "线程名:%s, 还有[%d]页数据没有获取！" % (threadName,temp_queue.qsize())
                logging.info(info)
                print(info)

                option = webdriver.ChromeOptions()
                option.add_argument("headless")
                browser = webdriver.Chrome(chrome_options=option)
                url = data_list_url
                url = url.format(26,curstart)

                print(url)
                logging.info(url)

                browser.get(url)  # Load page
                # time.sleep(1)     #休眠1秒，主要防止目标服务器判为攻击，不知是否有效

                #获得网页数据
                data = browser.page_source
                file_name = DATA_LIST_PATH  +"/"+ str(curstart) + ".html"
                if file_utils.write_file(file_name,data):
                    info = file_name + "写入文件成功"
                    logging.info(info)
                    print(info)

                # browser.close()
                browser.quit()
        except BaseException as e:
            traceback.print_exc()  #直接打印异常
            logging.error(traceback.format_exc()) #返回字符串 写入到文件



'''
批量获取数据
建议线程数不要超过5个
'''
class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self,thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        msg1 = "====Starting " + self.name
        logging.info(msg1)
        print(msg1)

        #get data
        get_data_list(self.name)

        msg2 = "====Exiting " + self.name
        logging.info(msg2)
        print(msg2)

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如果已经暂停的话
        self.__running.clear()  # 设置为False



'''
开始启动获取数据
'''
def start(threadCount):
    threads = []
    for i in range(threadCount):
        thread = myThread("thread-" + str(i))  # 区分其他线程名字
        # 添加线程到线程列表
        threads.append(thread)

    for t in threads:
        t.start()

    # # 等待所有线程完成
    for t in threads:
        if t.isAlive():
            t.join()
    info = "所有线程全部结束!"
    logging.info(info)
    print(info)

if __name__ == "__main__":

    '''
    判断数据是否已经获取完成
    '''
    data_count =  file_utils.get_curr_max_pageno(DATA_LIST_PATH)

    if  total_count  == data_count:
        print("数据已经全部采集完成：配置数据总量: %s,已采集数据总量: %s " % (total_count,data_count))
        print("程序已退出!")
        sys.exit(0)

    '''
    #1、初始化配置和数据
    '''
    init_data()

    '''
    #2、开始获取数据
    '''
    start(thread_count)
