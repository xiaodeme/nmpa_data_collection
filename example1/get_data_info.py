# coding=utf-8
import urllib2
import datetime
import time
import json
import os
import Queue
import threading
import logging

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from utils import etc_utils
from utils import access_data_utils
from utils import file_utils

#获取配置信息
dataTypeConfig = etc_utils.DataTypeConfig(26,"../etc/example1_data_type.cfg")
save_root_path = dataTypeConfig.get_save_root_path()
total_count = int(dataTypeConfig.get_total_count())

#data_list数据保存路径
DATA_LIST_PATH = save_root_path +  "/data_list/"
file_utils.mkdir_path(DATA_LIST_PATH)

# 器械详情保存路径
DATA_INFO_PATH = save_root_path +  "/data_info/"
file_utils.mkdir_path(DATA_INFO_PATH)

#日志保存路径
LOG_PATH =    save_root_path + "/logs/"
file_utils.mkdir_path(LOG_PATH)


#获取采集数据Id集合
file_list = file_utils.get_file_list(DATA_LIST_PATH)
id_list = file_utils.get_all_data_id(file_list)
print("采集数据总量:%s" % (id_list.qsize()))



'''
获取data_info数据
'''
def start(threadCount):
    # 启动60个线程，如果cfda官网服务拒绝链接，可适当将线程数量调小一点
    threads = []
    for i in range(threadCount):
        thread = myThread(i)  # 区分其他线程名字
        # 添加线程到线程列表
        threads.append(thread)

    for t in threads:
        t.start()

    # # 等待所有线程完成
    for t in threads:
        if t.isAlive():
            t.join()
    print "所有线程全部结束!"





def get_data_info(thread_name):



    while not id_list.empty():
        try:
            data_id = id_list.get()
            info = "线程名:%s,没有获取到数据还有 %d个" % (thread_name,id_list.qsize())
            print(info)

            # data_info保存文件名
            data_info_filename = "data_info_thread_%s.json" % (thread_name)
            data_info_filename = DATA_INFO_PATH + data_info_filename

            # 列表详情页url
            data_info_url = dataTypeConfig.get_data_info_url()
            data_info_url = data_info_url.format(dataTypeConfig.get_data_type(), data_id)

            # 数据采集并保存到本地
            data_info_data = access_data_utils.get_data(data_info_url)
            data_info_data = data_info_data.replace("\\n\\r", "").decode("gbk").encode("utf-8")

            with open(data_info_filename, 'a') as f:
                f.writelines(data_info_data + "\n")

            info = data_info_filename + "写入成功! id: " + data_id
            print(info)

            # 休眠1秒，防止服务器判断为攻击
            time.sleep(1)
            # logging.info(info)
        except urllib2.URLError as e:
            id_list.put(data_id)
            # time.sleep(6000)
            print("URLError")
            logging.error("URLError")
            logging.error(e.message)
        except UnboundLocalError as e:
            print("UnboundLocalError")
            logging.error("UnboundLocalError")
            logging.error(e.message)




class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        msg1 = "====Starting " + self.name
        print(msg1)
        logging.info(msg1)
        get_data_info(self.name)
        msg2 = "====Exiting " + self.name
        print(msg2)
        logging.info(msg2)

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False




if __name__ == "__main__":
    # file_list= file_utils.get_file_list(DATA_LIST_PATH)
    # id_list  = file_utils.get_all_data_id(file_list)
    # print("采集数据总量:%s" % (id_list.qsize()))
    # print("配置数据总量:%s" % (total_count))

    thread_count = int(dataTypeConfig.get_thread_count())
    start(thread_count)