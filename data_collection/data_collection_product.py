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
import  ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')
from utils import etc_utils
from utils import access_data_utils
from utils import file_utils
from utils import log_utils
from utils import config
import  Queue
#
# '''
# ==============
# 数据采集主程序:按id采集注册产品详细信息
# ==============
# '''
# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

def start(threadCount,config_dict):
    # 启动x个线程，建议小于10个
    threads = []
    for i in range(threadCount):
        # 区分其他线程名字
        thread = myThread(i,config_dict)
        # 添加线程到线程列表
        threads.append(thread)

    for t in threads:
        t.start()

    # # 等待所有线程完成
    for t in threads:
        if t.isAlive():
            t.join()
    logging.info("所有线程全部结束!")


def get_data_info(thread_name,config_dict):
    #新增数据保存路径
    data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    while not ADD_DATA_LIST.empty():
        try:
            data_id = ADD_DATA_LIST.get()
            info = "线程名:%s,没有获取到数据还有 %d个" % (thread_name,ADD_DATA_LIST.qsize())
            logging.info(info)

            # data_info保存文件名
            save_filename = "data_info_thread_%s.json" % (thread_name)
            save_filename = data_info_save_folder_name + save_filename

            # 列表详情页url
            get_key = "get_type_" + str(config_dict["get_type"])
            data_info_url = cf.get(get_key ,"data_info_url")
            data_info_url = data_info_url.format(config_dict["data_type"], data_id)

            # 数据采集并保存到本地
            data_info_data = access_data_utils.get_data(data_info_url)
            data_info_data = data_info_data.replace("\\n\\r", "").decode("gbk").encode("utf-8")

            #将数据标识和数据一起存储
            data = str(data_id) + "==" + data_info_data
            with open(save_filename, 'a') as f:
                f.writelines(data + "\n")

            info = save_filename + "写入成功! id: " + str(data_id)
            logging.debug(info)

            # 休眠1秒，防止服务器判断为攻击
            time.sleep(1)
        except urllib2.URLError as e:
            ADD_DATA_LIST.put(data_id)
            print("URLError")
            logging.error("URLError")
            logging.error(e.message)
        except UnboundLocalError as e:
            print("UnboundLocalError")
            logging.error("UnboundLocalError")
            logging.error(e.message)

class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, name,config_dict=dict):
        threading.Thread.__init__(self)
        self.name = name
        self.config_dict = config_dict
    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        msg1 = "====Starting " + self.name
        logging.info(msg1)
        get_data_info(self.name,self.config_dict)
        msg2 = "====Exiting " + self.name
        logging.info(msg2)

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False



#
# def check_data(config_dict):
#




if __name__ == "__main__":
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    # 日志初始化配置
    LOG_NAME = "data_collection.log"
    log_filename = config.get_curr_root_path(root_path,data_type) + LOG_NAME
    log_utils.log_config(log_filename)


    config_dict = config.get_config(root_path, data_type)


    # 获取待新增的数据
    add_folder_name = config_dict["add_folder_name"]
    add_filename = add_folder_name + "add_data.json"
    ADD_DATA_LIST = file_utils.get_add_data_id(add_filename)
    print ADD_DATA_LIST.qsize()

    start(8,config_dict)