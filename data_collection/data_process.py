#coding=utf-8
import os
import sys
sys.path.append('../')
import ConfigParser
import logging
from utils import file_utils
from utils import config
from utils import log_utils
# 读取基础配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")


'''
==============
数据处理主程序
==============
'''
ADD_DATA_FILENAME = "/add_data.json"
REDUCE_DATA_FILENAME = "/reduce_data.json"
#程序运行前生成的基础配置信息
CONFIG_FILENAME =  "config.ini"
def data_process(config_dict):
    """
    本次采集数据与当前数据库对比，将新增、减少数据存入add、reduct文件夹
    :param config_dict:
    :return:
    """
    add_filename = config_dict["add_folder_name"] + ADD_DATA_FILENAME
    reduce_filename = config_dict["reduct_folder_name"] + REDUCE_DATA_FILENAME
    data_list_folder_name = config_dict["data_list_folder_name"]

    if  os.path.exists(add_filename):
        logging.info("数据分析:本次新增减少[add/reduct]文件已经存储:%s" % (add_filename))
        return

    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    """
    获取上一天数据总量(上一天可能采集失败，继续循环获取上一天，直到获取数据)
    """
    last_date_num = 1
    last_date = file_utils.get_last_date(last_date_num)
    last_data_list_folder_name  = config.get_last_root_path(root_path,data_type,last_date)
    file_list = file_utils.get_file_list(last_data_list_folder_name +  "/data_list/")
    id_list = file_utils.get_data_info_id(file_list)
    curr_data_id_list =  list(id_list.queue)
    curr_data_id_list_len = len(curr_data_id_list)
    while curr_data_id_list_len == 0:
        logging.warn("数据分析:[%s]数据采集数量: %s" % (last_date, curr_data_id_list_len))

        last_date_num +=1
        last_date = file_utils.get_last_date(last_date_num)

        last_data_list_folder_name = config.get_last_root_path(root_path, data_type, last_date)
        file_list = file_utils.get_file_list(last_data_list_folder_name + "/data_list/")
        id_list = file_utils.get_data_info_id(file_list)
        curr_data_id_list = list(id_list.queue)
        curr_data_id_list_len = len(curr_data_id_list)


    logging.info("数据分析:[%s]数据采集数量: %s" % (last_date, curr_data_id_list_len))








    file_list = file_utils.get_file_list(data_list_folder_name)
    id_list = file_utils.get_data_info_id(file_list)
    new_data_id_list = list(id_list.queue)
    logging.info("数据分析:今天[%s]数据采集数量: %s" % (file_utils.get_curr_date(),len(new_data_id_list)))

    # 本次新增数据
    add_data= list(set(new_data_id_list).difference(set(curr_data_id_list)))  # b中有而a中没有的
    file_utils.write_file(add_filename,str(add_data))
    logging.info("数据分析:本次新增数据:%s" % (len(add_data)))
    if len(add_data) > 0:
        logging.info("本次新增数据标识已经保存")

    # 本次减少数据
    reduce_data =  list(set(curr_data_id_list).difference(set(new_data_id_list)))  # a中有而b中没有的
    file_utils.write_file(reduce_filename, str(reduce_data))
    logging.info("数据分析:本次减少数据:%s" %(len(reduce_data)))
    if len(reduce_data) > 0:
        logging.info("本次减少数据标识已经保存")



if __name__ == "__main__":

    pass

    # # 运行程序基础参数
    # config_filename = cf.get("default_config", "config_filename")
    # log_name = cf.get("default_config", "log_name")
    # get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效,未来可能需要实现方式
    # data_type = cf.get("base_config", "data_type")
    # root_path = cf.get("base_config", "root_path")
    #
    # #0.当前数据采集存储路径
    # curr_date = file_utils.get_curr_date()
    # curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)
    #
    # #1.读取配置信息
    # config_dict = None
    # if not os.path.exists(curr_root_path + config_filename):
    #     print("程序运行基础配置信息:%s:未初始化，请先运行init.py!" % (config_filename))
    #     sys.exit(0)
    # else:
    #     config_dict = config.get_config(root_path,data_type,curr_date)
    #
    # # 2.初始化日志
    # log_utils.log_config(curr_root_path + log_name)
    #
    # logging.info("当前执行文件:%s" % (os.path.basename(__file__)))
    #
    # #3. 数据分析3
    # data_process(config_dict)






