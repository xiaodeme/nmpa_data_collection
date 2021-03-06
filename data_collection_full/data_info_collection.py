# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('../')
import urllib2
import time
import threading
import logging
import  ConfigParser
from utils import access_data_utils
from utils import file_utils
from utils import log_utils
from utils import config
import os
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
    while not DATA_LIST.empty():
        try:
            data_id = DATA_LIST.get()
            info = "线程名:%s,没有获取到数据还有 %d个" % (thread_name,DATA_LIST.qsize())
            logging.info(info)

            # data_info保存文件名
            save_filename = "data_info_thread_%s.json" % (thread_name)
            save_filename = data_info_save_folder_name + save_filename

            # 列表详情页url
            data_info_url = cf.get("access_url" ,"data_info_url")
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

            # 休眠2秒，防止服务器判断为攻击
            time.sleep(2)
        except urllib2.URLError as e:
            DATA_LIST.put(data_id)
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

if __name__ == "__main__":
    # 运行程序基础参数
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效,未来可能需要实现方式
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    # 0.当前数据采集存储路径
    curr_date = file_utils.get_curr_date()
    curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)

    # 1.读取配置信息
    if not os.path.exists(curr_root_path + config_filename):
        print("程序运行基础配置信息:%s:未初始化，请先运行init.py!" % (config_filename))
        sys.exit(0)
    else:
        config_dict = config.get_config(root_path, data_type, curr_date)

    # 2.初始化日志
    log_utils.log_config(curr_root_path + log_name)

    # 3. 获取待新增的数据
    data_list_folder_name = config_dict["data_list_folder_name"]
    file_list = file_utils.get_file_list(data_list_folder_name)
    DATA_LIST = file_utils.get_data_info_id(file_list)
    add_data_count = DATA_LIST.qsize()
    logging.info("[data_info]采集日期=%s,计划新增数据采集数据总量=:%s" % (curr_date, add_data_count))

    # data_info > save 数据采集总量检查
    data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    file_list = file_utils.get_file_list(data_info_save_folder_name)
    data_info_count = file_utils.data_info_count(file_list)
    logging.info("[data_info]采集日期=%s,实际新增数据采集数据总量=:%s" % (curr_date, data_info_count))


    if add_data_count == data_info_count:
        logging.info("采集日期=%s,新增数据采集已经完成!" % (curr_date))
        sys.exit(0)
    else:
        data_info_save_folder_name = config_dict["data_info_save_folder_name"]
        if file_utils.clear_folder(data_info_save_folder_name):
            logging.info("清空文件夹文件:%s" % (data_info_save_folder_name))
        start(10, config_dict)
        # pass
