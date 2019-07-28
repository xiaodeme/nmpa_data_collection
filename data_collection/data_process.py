#coding=gbk
import os
import sys
sys.path.append('../')
import ConfigParser
import logging
from utils import file_utils
from utils import config
from utils import log_utils
# ��ȡ���������ļ�
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")


'''
==============
���ݴ���������
==============
'''
ADD_DATA_FILENAME = "/add_data.json"
REDUCE_DATA_FILENAME = "/reduce_data.json"
#��������ǰ���ɵĻ���������Ϣ
CONFIG_FILENAME =  "config.ini"
def data_process(config_dict):
    """
    ���βɼ������뵱ǰ���ݿ�Աȣ����������������ݴ���add��reduct�ļ���
    :param config_dict:
    :return:
    """
    add_filename = config_dict["add_folder_name"] + ADD_DATA_FILENAME
    reduce_filename = config_dict["reduct_folder_name"] + REDUCE_DATA_FILENAME
    data_list_folder_name = config_dict["data_list_folder_name"]

    if  os.path.exists(add_filename):
        logging.info("���ݷ���:������������[add/reduct]�ļ��Ѿ��洢:%s" % (add_filename))
        return

    last_data_list_folder_name  = config.get_last_root_path(root_path,data_type)
    file_list = file_utils.get_file_list(last_data_list_folder_name +  "/data_list/")
    id_list = file_utils.get_data_info_id(file_list)
    curr_data_id_list =  list(id_list.queue)
    logging.info("���ݷ���:��һ��[%s]���ݲɼ�����: %s" %  (file_utils.get_last_date(),len(curr_data_id_list)))

    file_list = file_utils.get_file_list(data_list_folder_name)
    id_list = file_utils.get_data_info_id(file_list)
    new_data_id_list = list(id_list.queue)
    logging.info("���ݷ���:����[%s]���ݲɼ�����: %s" % (file_utils.get_curr_date(),len(new_data_id_list)))

    # ������������
    add_data= list(set(new_data_id_list).difference(set(curr_data_id_list)))  # b���ж�a��û�е�
    file_utils.write_file(add_filename,str(add_data))
    logging.info("���ݷ���:������������:%s" % (len(add_data)))

    # ���μ�������
    reduce_data =  list(set(curr_data_id_list).difference(set(new_data_id_list)))  # a���ж�b��û�е�
    file_utils.write_file(reduce_filename, str(reduce_data))
    logging.info("���ݷ���:���μ�������:%s" %(len(reduce_data)))




if __name__ == "__main__":

    # ���г����������
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # �ò�����ʱδ��Ч,δ��������Ҫʵ�ַ�ʽ
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    #0.��ǰ���ݲɼ��洢·��
    curr_date = file_utils.get_curr_date()
    curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)

    #1.��ȡ������Ϣ
    config_dict = None
    if not os.path.exists(curr_root_path + config_filename):
        print("�������л���������Ϣ:%s:δ��ʼ������������init.py!" % (config_filename))
        sys.exit(0)
    else:
        config_dict = config.get_config(root_path,data_type,curr_date)

    # 2.��ʼ����־
    log_utils.log_config(curr_root_path + log_name)

    #3. ���ݷ���3
    data_process(config_dict)






