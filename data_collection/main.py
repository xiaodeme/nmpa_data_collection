#coding=utf-8
import sys
sys.path.append('../')

from utils import config
import data_list_collection
import ConfigParser

# 读取基础配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

#日志文件
LOG_NAME = "data_collection.log"

if __name__ == "__main__":
    #运行程序基础参数
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    # 第一步：初始化程序运行配置基础信息
    config.init_config(root_path, data_type,get_type)

    # 第二步：获取程序运行配置基础信息
    config_dict = config.get_config(root_path,data_type)

    # 第三步：运行数据采集程序
    data_list_collection.data_collection(config_dict)

    #第四步：数据处理
    # data_process.data_process(config_dict)

    #第五步：启动新增数据采集程序 data_collection_new_data.py
    # run data_collection_product

    pass





