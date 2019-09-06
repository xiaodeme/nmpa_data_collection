# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 23:52
# @Author  : xiaodeme
# @Email   : xiaodeme@163.com
# @File    : data_collection_get_new_data.py
# @Software: PyCharm

import urllib2
import time
import threading
import logging
import sys
import  ConfigParser
reload(sys)
import os
sys.path.append('../')
sys.setdefaultencoding('utf-8')
from utils import access_data_utils
from utils import file_utils
from utils import log_utils
from utils import config
#
# '''
# ==============
# 数据采集主程序:按id采集注册产品详细信息
# ==============
# '''
# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

def get_data_info(NEW_DATA_LIST,config_dict):

    #新增数据保存路径
    data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    # 清空data_info > save文件夹
    if file_utils.clear_folder(data_info_save_folder_name):
        logging.info("清空文件夹文件:%s" % (data_info_save_folder_name))


    while not NEW_DATA_LIST.empty():
        try:
            data_id = NEW_DATA_LIST.get()
            info = "没有获取到数据还有 %d个" % (NEW_DATA_LIST.qsize())
            logging.info(info)

            # data_info保存文件名
            save_filename = "get_new_data.json"
            save_filename = data_info_save_folder_name + save_filename

            # 列表详情页url
            data_info_url = cf.get("access_url" ,"data_info_url")
            data_info_url = data_info_url.format(config_dict["data_type"], data_id)

            # 数据采集并保存到本地
            data_info_data = access_data_utils.get_data(data_info_url)
            # access_data_utils.get_test_timeout()
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
            logging.error("获取新增数据采集失败! %s" %(e.args))
            raise e


def get_new_data(config_dict):
    """
    获取当日新增数据
    :param config_dict:
    :return:
    """
    curr_date = file_utils.get_curr_date()


    add_folder_name = config_dict["add_folder_name"]
    add_filename = add_folder_name + "add_data.json"
    NEW_DATA_LIST = file_utils.get_add_data_id(add_filename)
    add_data_count = NEW_DATA_LIST.qsize()
    # logging.info("[data_info]采集日期=%s,计划新增数据采集数据总量=:%s" % (curr_date, add_data_count))

    # data_info > save 数据采集总量检查
    data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    file_list = file_utils.get_file_list(data_info_save_folder_name)
    data_info_count = file_utils.data_info_count(file_list)
    # logging.info("[data_info]采集日期=%s,实际新增数据采集数据总量=:%s" % (curr_date, data_info_count))

    #数据采集前判断是否已经采集完成
    if add_data_count == data_info_count:
        logging.info("采集日期=%s,新增数据采集已经完成!" % (curr_date))
        return 1

    try:
        logging.info("开始采集今日[%s]新增数据" % (curr_date))
        get_data_info(NEW_DATA_LIST,config_dict)
        return 1

    except BaseException, e:
        return -1



if __name__ == "__main__":

    pass

    # # 运行程序基础参数
    # config_filename = cf.get("default_config", "config_filename")
    # log_name = cf.get("default_config", "log_name")
    # get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效,未来可能需要实现方式
    # data_type = cf.get("base_config", "data_type")
    # root_path = cf.get("base_config", "root_path")
    #
    # # 0.当前数据采集存储路径
    # curr_date = file_utils.get_curr_date()
    # curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)
    #
    # # 1.读取配置信息
    # config_dict = None
    # if not os.path.exists(curr_root_path + config_filename):
    #     print("程序运行基础配置信息:%s:未初始化，请先运行init.py!" % (config_filename))
    #     sys.exit(0)
    # else:
    #     config_dict = config.get_config(root_path, data_type, curr_date)
    #
    # # 2.初始化日志
    # log_utils.log_config(curr_root_path + log_name)
    #
    # logging.info("当前执行文件:%s" % (os.path.basename(__file__)))
    #
    #
    # #3. 获取待新增的数据
    # add_folder_name = config_dict["add_folder_name"]
    # add_filename = add_folder_name + "add_data.json"
    # ADD_DATA_LIST = file_utils.get_add_data_id(add_filename)
    # add_data_count  = ADD_DATA_LIST.qsize()
    # logging.info("[data_info]采集日期=%s,计划新增数据采集数据总量=:%s" % (curr_date, add_data_count))
    #
    # # data_info > save 数据采集总量检查
    # data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    # file_list = file_utils.get_file_list(data_info_save_folder_name)
    # data_info_count = file_utils.data_info_count(file_list)
    # logging.info("[data_info]采集日期=%s,实际新增数据采集数据总量=:%s" % (curr_date, data_info_count))
    #
    # if add_data_count == data_info_count:
    #     logging.info("采集日期=%s,新增数据采集已经完成!" %(curr_date))
    #     sys.exit(0)
    # else:
    #     data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    #     if file_utils.clear_folder(data_info_save_folder_name):
    #         logging.info("清空文件夹文件:%s" % (data_info_save_folder_name))
    #     start(10,config_dict)