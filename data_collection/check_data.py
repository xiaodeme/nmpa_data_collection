#coding=utf-8
import sys
import os
sys.path.append('../')
reload(sys)
sys.setdefaultencoding('utf-8')
import ConfigParser
import logging
from utils import file_utils
from db_manager import  dbManager
from utils import config
from utils import log_utils
from utils import  comm_utils
# 读取基础配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

#程序运行前生成的基础配置信息
CONFIG_FILENAME =  "config.ini"

#日志文件
LOG_NAME = "data_collection.log"

def check_data(curr_date):
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")
    config_dict = config.get_config(root_path, data_type, curr_date)

    # 日志初始化配置
    log_filename = config.get_curr_root_path(root_path, data_type, curr_date) + "/logs/" + LOG_NAME
    log_utils.log_config(log_filename)

    # 3. 获取待新增的数据
    add_folder_name = config_dict["add_folder_name"]
    add_filename = add_folder_name + "add_data.json"
    ADD_DATA_LIST = file_utils.get_add_data_id(add_filename)
    add_data_count = ADD_DATA_LIST.qsize()
    logging.info("[data_info]采集日期=%s,计划新增数据采集数据总量=:%s" % (curr_date, add_data_count))

    # data_info > save 数据采集总量检查
    data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    file_list = file_utils.get_file_list(data_info_save_folder_name)
    data_info_count = file_utils.data_info_count(file_list)
    logging.info("[data_info]采集日期=%s,实际新增数据采集数据总量=:%s" % (curr_date, data_info_count))

if __name__ == "__main__":
    """
        用于查看统计当前数据新增采集情况
    """
    curr_date = file_utils.get_curr_date()
    check_data(curr_date)
