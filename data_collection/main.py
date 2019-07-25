#coding=utf-8
from utils import file_utils
from utils import config
from utils import log_utils
import data_collection
import data_process
import logging

#日志文件
LOG_NAME = "data_collection.log"

if __name__ == "__main__":
    print("==========欢迎使用NMPA数据采集程序=============")

    #运行程序基础参数
    get_type = 1   #该参数暂时未生效
    data_type = 26
    root_path = '~/data/data_source/'

    # 第一步：初始化程序运行配置基础信息
    config.init_config(root_path, data_type,get_type)

    # 第二步：获取程序运行配置基础信息
    config_dict = config.get_config(root_path,data_type)

    # 第三步：运行数据采集程序
    data_collection.data_collection(config_dict)

    #第四步：数据处理
    data_process.data_process(config_dict)

    #第五步：启动新增数据采集程序 data_collection_product.py
    # run data_collection_product

    #config.py
    #data_collection.py
    #data_process.py
    #data_collection_product.py
    pass





