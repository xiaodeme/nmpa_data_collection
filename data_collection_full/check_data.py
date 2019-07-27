#coding=utf-8
import sys
import os
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

    #data_info 数据采集总量检查
    data_list_folder_name = config_dict["data_list_folder_name"]
    data_type = config_dict["data_type"]
    file_list = file_utils.get_file_list(data_list_folder_name)
    id_list = file_utils.get_data_info_id(file_list)
    qsize = id_list.qsize()
    logging.info("[data_list]采集日期=%s,数据采集数据总量=:%s" % (curr_date,qsize))

    # data_info > save 数据采集总量检查
    data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    file_list = file_utils.get_file_list(data_info_save_folder_name)
    data_info_count = file_utils.data_info_count(file_list)
    logging.info("[data_info]采集日期=%s,数据采集数据总量=:%s" % (curr_date,data_info_count))

    #NMPA官网数据总量检查
    total_count = comm_utils.get_curr_nmpa_total_count(data_type)
    logging.info("[NMPA官网]当前日期=%s,数据总量=:%s" % (file_utils.get_curr_date(),total_count))


if __name__ == "__main__":
    """
        用于查看统计当前数据采集情况
    """
    curr_date = file_utils.get_curr_date()
    # curr_date = "20190726"
    check_data(curr_date)
