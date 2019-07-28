#coding=gbk
import os
import sys
sys.path.append('../')
from utils import  file_utils
from utils import config
import ConfigParser
import logging
# ��ȡ���������ļ�
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")
if __name__ == "__main__":

    # ���г����������
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # �ò�����ʱδ��Ч,δ��������Ҫʵ�ַ�ʽ
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")
    curr_date = file_utils.get_curr_date()
    # curr_date = "20190727"
    curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)

    tips = "===============================\n" \
           "��������ǰ�ȶ�base_config.ini�������ã�\n" \
           "https://github.com/xiaodeme    \n" \
           "������־��鿴 logs/data_collection.log    \n" \
           "==============================="
    print tips
    #
    os.system("python ./init.py")
    os.system("python ./data_list_collection.py")
    os.system("python ./data_process.py")
    os.system("python ./data_collection_new_data.py")
    os.system("python ./check_data.py")

    config_dict = config.get_config(root_path, data_type, curr_date)
    tips = "===============================\n" \
           "���ݲɼ��洢��·��:%s \n" \
           "���ݲɼ��б���Ϣ·����%s \n" \
           "���ݲɼ���ϸ��Ϣ·����%s \n" \
           "��������������ϸ��Ϣ·����%s \n" \
           "�������������ϸ��Ϣ·����%s \n" \
           "==============================="
    print(tips % (root_path
                  , config_dict["data_list_folder_name"]
                  , config_dict["data_info_save_folder_name"]
                  , config_dict["add_folder_name"]
                  , config_dict["reduct_folder_name"]
                  ))