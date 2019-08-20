#coding=utf-8
import sys
sys.path.append('../')
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from utils import config
from utils import access_data_utils
from utils import comm_utils
from utils import log_utils
from utils import file_utils
import logging
import time
import  ConfigParser
# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")
'''
==============
数据采集主程序:采集数据列表信息
==============
'''
def save_data_list_to_disk(config_dict):
    data_type = int(config_dict["data_type"])
    get_type = int(config_dict["get_type"])
    data_list_folder_name  =  config_dict["data_list_folder_name"]
    if file_utils.clear_folder(data_list_folder_name):
        logging.info("清空文件夹文件:%s" % (data_list_folder_name))

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
        data_list_filename = data_list_folder_name + data_list_filename

        # 列表页url(从配置文件读取)
        data_list_url = cf.get("access_url" ,"data_list_url")
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
    logging.info("查询[data_list]文件夹中数据已采集总量=:%s" % (qsize))
    try:
        # comm_utils.access_data_utils.get_test_timeout()

        total_count = comm_utils.get_curr_nmpa_total_count(data_type)
        logging.info("查询当前NMPA官网数据总量=:%s" % (total_count))
        if qsize == total_count:
            return True
        else:
            return False
        return True
    except BaseException ,e :
        logging.error("查询当前NMPA官网数据总量查询失败!")
        logging.error("查询当前NMPA官网数据超时>>>>%s" % (e.args))
        raise e





def data_collection(config_dict):
    """
    :param config_dict: 程序运行基础配置信息
    :return:
    """
    try:
        #数据检查
        result  = check_data(config_dict)
        if result:
            logging.info("统计[data_list]数据总量与[当前NMPA官网数据总量]相等，数据集已经完成采集!")
        else:
            #开始数据采集
            save_data_list_to_disk(config_dict)
        return 1
    except BaseException, e:
        return 0


#程序运行前生成的基础配置信息
if __name__ == "__main__":
    # if len(sys.argv) <> 3:
    #     print("运行程序需要2个参数 get_type = {1,2} data_type = {25,26}")
    #     print("运行示例:python data_list_collection.py 1 26")
    '''
    ======================================================
    :todo
    get_type: 数据获取方式
            1 urllib2方式
            2 selenium方式
    data_type:数据采集类型 
            26 国产器械  
            27 进口器械
    root_path:文件存储路径
    =====================================================
    # '''
    #运行程序基础参数
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效,未来可能需要实现方式
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    #0.当前数据采集存储路径
    curr_date = file_utils.get_curr_date()
    curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)

    #1.读取配置信息
    config_dict = None
    if not os.path.exists(curr_root_path + config_filename):
        print("程序运行基础配置信息:%s:未初始化，请先运行init.py!" % (config_filename))
        sys.exit(0)
    else:
        config_dict = config.get_config(root_path,data_type,curr_date)

    #2.初始化日志
    log_utils.log_config(curr_root_path + log_name)

    logging.info("当前执行文件:%s" %( os.path.basename(__file__) ))

    #3.开始采集
    data_collection(config_dict)

