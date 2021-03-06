#coding=utf-8
import os
import ast
from utils import file_utils
from utils import log_utils
import logging

#程序运行前生成的基础配置信息
CONFIG_FILENAME =  "config.ini"

#日志文件
LOG_NAME = "data_collection.log"

def get_config(root_path = str,data_type=int,curr_date=str):
    """
    按指定日期返回程序运行配置文件
    :param root_path:
    :param data_type:
    :param curr_date:
    :return:
    """
    config_filename = get_curr_root_path(root_path,data_type,curr_date) + CONFIG_FILENAME
    if not os.path.exists(config_filename):
        logging.error("指定日期=%s,不存在配置信息!" % (curr_date))
        return False

    with open(config_filename, "r") as f:
       dict =  ast.literal_eval(f.read())

    return dict

def init_config(root_path,data_type,get_type):
    """
    初始化程序运行前基础配置信息
    :todo 后续实现参数校验
    :param root_path: 文件存储根路径
    :param data_type: 数据采集类型  26 国产器械  27 进口器械
    :param get_type:  数据获取方式 1 urllib2方式 2 selenium方式
    :return:
    """
    curr_date = file_utils.get_curr_date()
    curr_root_path = get_curr_root_path(root_path, data_type,curr_date)

    #日志初始化配置
    # log_foloder_name =  curr_root_path  + "/logs/"
    # file_utils.mkdir_path(log_foloder_name)
    # log_utils.log_config(log_foloder_name + LOG_NAME)

    # 当前数据存储根路径(定时执行， 按日期存放)
    if os.path.exists(curr_root_path + CONFIG_FILENAME):
        # print("本次数据采集[程序运行基础配置信息:%s]:已经初始完成!" % (CONFIG_FILENAME))
        logging.info("本次数据采集[程序运行基础配置信息:[%s]:已经初始化完成!" % (curr_root_path+CONFIG_FILENAME))
        return False

    # 初始数据存储路径
    data_list_folder_name = curr_root_path + "/data_list/"
    data_info_folder_name = curr_root_path + "/data_info/"
    add_folder_name = data_info_folder_name + "/add/"
    reduct_folder_name = data_info_folder_name + "/reduct/"
    data_info_save_folder_name = data_info_folder_name + "/save/"

    # 创建list、info文件夹
    file_utils.mkdir_path(data_list_folder_name)
    file_utils.mkdir_path(data_info_folder_name)

    # 创建data_info > add 、reduct 文件夹
    file_utils.mkdir_path(add_folder_name)
    file_utils.mkdir_path(reduct_folder_name)

    # 创建save文件夹(最终会入库的信息)
    file_utils.mkdir_path(data_info_save_folder_name)

    config_dict = {'data_type':data_type,
                    'get_type':get_type,
                    'root_path': root_path,
                   'data_list_folder_name': data_list_folder_name,
                   'data_info_folder_name': data_info_folder_name,
                   'add_folder_name': add_folder_name,
                   'reduct_folder_name': reduct_folder_name,
                   'data_info_save_folder_name': data_info_save_folder_name
                   }

    config_filename = curr_root_path + "/" + CONFIG_FILENAME
    file_utils.write_file(config_filename, str(config_dict))

    logging.info("程序运行基础配置信息初始化完成:%s" % (config_filename))
    logging.debug(str(config_dict))

def get_last_root_path(root_path,data_type,last_date):
    """
    获取当前执行根路径: 当前路径 = 配置根路径 + 当前数据类型(data_type)  + 当前日期
    :param root_path:配置根路径
    :param data_type:数据类型
    :return:
    """
    last_root_path = root_path + "/" + str(data_type) + "/" + last_date + "/"
    return last_root_path


def get_curr_root_path(root_path,data_type,curr_date):
    """
    获取当前执行根路径: 当前路径 = 配置根路径 + 当前数据类型(data_type)  + 当前日期
    :param root_path:配置根路径
    :param data_type:数据类型
    :param curr_date:可指定日期(格式：yyyymm)，当为None时，生成当前日期
    :return:
    """
    if  curr_date is None:
        curr_date = file_utils.get_curr_date()
    curr_root_path = root_path + "/" + str(data_type) + "/" + curr_date + "/"
    return curr_root_path



if __name__ == "__main__":
    print get_curr_root_path("e:/",26,None)
    pass

    # root_path = 'E:/data/data_source/26/'
    # # init_file_path(root_path)
    # dict = get_folder_name(root_path)
    # print dict["data_list_folder_name"]
    # print dict["data_info_folder_name"]
    # print dict["add_folder_name"]
    # print dict["reduct_folder_name"]
    # print dict["data_info_save_folder_name"]

