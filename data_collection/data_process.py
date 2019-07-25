#coding=utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
import ConfigParser
import logging
import time
from utils import access_data_utils
from utils import file_utils
from utils import comm_utils
from db_manager import  dbManager
import data_collection_product
from utils import config
from utils import log_utils
'''
==============
数据处理主程序
==============
'''

ADD_DATA_FILENAME = "/add_data.json"
REDUCE_DATA_FILENAME = "/reduce_data.json"

def data_process(config_dict):
    add_filename = config_dict["add_folder_name"] + ADD_DATA_FILENAME
    reduce_filename = config_dict["reduct_folder_name"] + REDUCE_DATA_FILENAME
    data_list_folder_name = config_dict["data_list_folder_name"]

    if os.path.exists(add_filename):
        logging.info("本次新增减少文件已经存储:%s" % (add_filename))
        return

    curr_data_id_list = dbManager.get_curr_ids()
    logging.info("数据库已经采集数据数量: %s" %  (len(curr_data_id_list)))

    file_list = file_utils.get_file_list(data_list_folder_name)
    id_list = file_utils.get_all_data_id(file_list)
    new_data_id_list = list(id_list.queue)
    logging.info("本次数据采集总量:%s" % (len(new_data_id_list)))


    #本次新增数据
    add_data= list(set(new_data_id_list).difference(set(curr_data_id_list)))  # b中有而a中没有的
    logging.info("本次新增数据:%s" % (len(add_data)))
    file_utils.write_file(add_filename,str(add_data))


    #本次减少数据
    reduce_data =  list(set(curr_data_id_list).difference(set(new_data_id_list)))  # a中有而b中没有的
    file_utils.write_file(reduce_filename, str(reduce_data))
    logging.info("本次减少数据:%s" %(len(reduce_data)))




if __name__ == "__main__":
     # print("请运行main.py")

     get_type = 1  # 该参数暂时未生效
     data_type = 26
     root_path = '/home/wlin/data/data_source/'

     LOG_NAME = "data_collection.log"
     log_utils.log_config(root_path, data_type, LOG_NAME)

     config_dict = config.get_config(root_path, data_type)
     data_process(config_dict)






