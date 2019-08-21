# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 23:06
# @Author  : xiaodeme
# @Email   : xiaodeme@163.com
# @File    : start.py.py
# @Software: PyCharm

import os
import sys
sys.path.append('../')
import logging
import ConfigParser

from utils import  file_utils
from utils import log_utils
from utils import config
import data_list_collection
import data_process
import data_collection_get_new_data
import  check_data



# 读取基础配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

#日志文件
LOG_NAME = "data_collection.log"
if __name__ == "__main__":
    # 运行程序基础参数
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效,未来可能需要实现方式
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")
    curr_date = file_utils.get_curr_date()
    curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)
    tips = "===============================\n" \
           "程序运行前先对base_config.ini进行配置：\n" \
           "https://github.com/xiaodeme    \n" \
           "运行日志请查看 logs/data_collection.log    \n" \
           "==============================="
    print tips

    # 日志初始化配置
    log_foloder_name = curr_root_path + "/logs/"
    file_utils.mkdir_path(log_foloder_name)
    log_utils.log_config(log_foloder_name + LOG_NAME)


    #1. 初始化程序运行配置基础信息
    config.init_config(root_path, data_type, get_type)
    config_dict = config.get_config(root_path, data_type, curr_date)

    #2. 开始采集
    run_result = data_list_collection.data_collection(config_dict)
    if run_result < 1:
        logging.error("[1]执行不成功，终止程序运行:%s" % (run_result))

        #清空当天文件夹
        data_list_folder_name = config_dict["data_list_folder_name"]
        if file_utils.clear_folder(data_list_folder_name):
            logging.info("清空文件夹文件:%s" % (data_list_folder_name))

        logging.error("今天[%s]数据采集不成功,请重新运行采集程序!" %(curr_date))
        sys.exit(0)

    #3.数据分析
    data_process.data_process(config_dict)


    #4.新增数据采集
    run_result = data_collection_get_new_data.get_new_data(config_dict)
    if run_result < 1:
        logging.error("[2]执行不成功，终止程序运行:%s" % (run_result))
        sys.exit(0)

    # 5.数据采集检查
    check_data.check_data(curr_date)