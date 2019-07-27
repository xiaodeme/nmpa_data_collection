# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('../')
from utils import access_data_utils
from utils import config
from utils import comm_utils
from utils import log_utils
from utils import file_utils
import logging
import time
import  ConfigParser
import os
# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")
'''
==============
数据采集主程序:采集数据列表信息
==============
'''
def save_data_list_to_disk(forder_dict):
    data_type = int(forder_dict["data_type"])
    get_type = int(forder_dict["get_type"])
    begin_time = time.time()
    logging.info("数据采集开始时间:%s"  %  (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    # 当前官网数据总量
    total_count = comm_utils.get_curr_nmpa_total_count(data_type)
    # 每页显示总数量(即每个文件保存1000条数据)
    page_size = 1000;
    if total_count < page_size:
        page_size = total_count

    # 计算共多少页
    if total_count % page_size == 0:
        total_page_no = total_count / page_size
    else:
        total_page_no = total_count / page_size + 1
    # logging("数据总量=%s,每页采集量=%s，共计%s页:" % (total_count,page_size,total_page_no))
    logging.info("当前NMPA官网数据:data_type=%s,数据总量=%s,每页采集量%s,共计%s页" % (data_type, total_count,page_size,total_page_no))
    for index in range(total_page_no):
        page_index = index + 1

        # data_list保存文件名(文件按页码存储，每页PAGE_SIZE条)
        data_list_filename = "data_list_%s_%s.json" % (data_type,page_index)
        data_list_filename = forder_dict["data_list_folder_name"] + data_list_filename

        # 列表页url(从配置文件读取)
        get_key = "get_type_" + str(get_type)
        data_list_url = cf.get(get_key ,"data_list_url")
        data_list_url = data_list_url.format(data_type, page_index, page_size)
        logging.debug("数据采集地址:%s" % (data_list_url))

        # 数据采集并保存到本地
        data_list_data = access_data_utils.get_data(data_list_url)
        file_utils.write_file(data_list_filename, data_list_data)
        logging.debug("写入文件成功:%s" % (data_list_filename))
        logging.info("第%s页数据采集完成,剩余%s页,保存路径:%s" % (page_index,(total_page_no-page_index),data_list_filename))
        time.sleep(2)
    end_time = time.time()
    logging.info("数据采集结束时间:%s"  % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    logging.info("数据采集共计耗时:%s秒"  % (end_time - begin_time))



def check_data(config_dict):
    data_list_folder_name = config_dict["data_list_folder_name"]
    data_type = config_dict["data_type"]

    file_list = file_utils.get_file_list(data_list_folder_name)
    id_list = file_utils.get_data_info_id(file_list)

    qsize = id_list.qsize()
    logging.info("本次实际采集数据总量=:%s" % (qsize))
    total_count = comm_utils.get_curr_nmpa_total_count(data_type)
    logging.info("当前NMPA官网数据总量=:%s" % (total_count))

    if qsize == total_count:
        return True
    else:
        return False


def data_collection(config_dict):
    """
    :param forder_dict: 程序运行基础配置信息
    :return:
    """
    #数据采集
    save_data_list_to_disk(config_dict)

    #数据检查
    if check_data(config_dict):
        result = "数据采集结果:数据采集成功!"
        logging.info(result)
        # 执行数据处理程序 data_process.py

    else:
        result = "数据采集结果:数据采集失败!数据可能需要重新采集!"
        logging.info(result)

#程序运行前生成的基础配置信息
CONFIG_FILENAME =  "config.ini"
#日志文件
LOG_NAME = "data_collection.log"

if __name__ == "__main__":
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")
    # # 官网数据与已采集数据相等则不继续执行

    # 日志初始化配置
    log_filename = config.get_curr_root_path(root_path,data_type) +"/logs/"+ LOG_NAME
    log_utils.log_config(log_filename)

    curr_root_path = config.get_curr_root_path(root_path, data_type)
    if not os.path.exists(curr_root_path + CONFIG_FILENAME):
        logging.error("程序运行基础配置信息:%s:为初始化，请先运行init.py!" % (CONFIG_FILENAME))
        sys.exit(0)

    # 文件存储相关路径信息
    forder_dict = config.get_config(root_path,data_type)

    # 数据采集
    data_collection(forder_dict)