#coding=utf-8
import logging
from utils import  file_utils


def log_config(root_path ,data_type,log_name):
    '''
    日志配置：存储路径 = 配置根路径 + 数据类型 + logs
    :todo 后续考虑日志按天生成
    :param root_path:
    :param data_type:
    :param log_name:
    :return:
    '''
    log_foloder_name = root_path  + "/" +  str(data_type) + "/" + "/logs/"
    file_utils.mkdir_path(log_foloder_name)
    filename = log_foloder_name + log_name
    logging.basicConfig(filename=filename, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

