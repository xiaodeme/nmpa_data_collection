#coding=gbk
import sys
sys.path.append('../')
from utils import config
import ConfigParser

# ��ȡ���������ļ�
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

if __name__ == "__main__":
    #���г����������
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # �ò�����ʱδ��Ч
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    #��ʼ�������������û�����Ϣ
    config.init_config(root_path, data_type,get_type)


