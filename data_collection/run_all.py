#coding=utf-8
import os
import sys
sys.path.append('../')
from utils import  file_utils
from utils import config
import ConfigParser
# 读取基础配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")
if __name__ == "__main__":

    # 运行程序基础参数
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效,未来可能需要实现方式
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")
    curr_date = file_utils.get_curr_date()
    # curr_date = "20190727"
    curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)
    tips = "===============================\n" \
           "程序运行前先对base_config.ini进行配置：\n" \
           "https://github.com/xiaodeme    \n" \
           "运行日志请查看 logs/data_collection.log    \n" \
           "==============================="
    print tips
    #
    os.system("python ./init.py")
    os.system("python ./data_list_collection.py")
    os.system("python ./data_process.py")
    os.system("python ./data_collection_new_data.py")
    os.system("python ./check_data.py")

    config_dict = config.get_config(root_path, data_type, curr_date)
    tips = "===============================\n" \
           "数据采集存储根路径:%s \n" \
           "数据采集列表信息路径：%s \n" \
           "数据采集详细信息路径：%s \n" \
           "当天新增数据详细信息路径：%s \n" \
           "当天减少数据详细信息路径：%s \n" \
           "==============================="
    print(tips % (root_path
                  , config_dict["data_list_folder_name"]
                  , config_dict["data_info_save_folder_name"]
                  , config_dict["add_folder_name"]
                  , config_dict["reduct_folder_name"]
                  ))