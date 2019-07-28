#coding=utf-8
import sys
sys.path.append('../')
from utils import config
import ConfigParser

# 读取基础配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

if __name__ == "__main__":
    #运行程序基础参数
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    #初始化程序运行配置基础信息
    config.init_config(root_path, data_type,get_type)


