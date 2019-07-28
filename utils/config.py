#coding=gbk
import os
import ast
from utils import file_utils
from utils import log_utils
import logging

#��������ǰ���ɵĻ���������Ϣ
CONFIG_FILENAME =  "config.ini"

#��־�ļ�
LOG_NAME = "data_collection.log"

def get_config(root_path = str,data_type=int,curr_date=str):
    """
    ��ָ�����ڷ��س������������ļ�
    :param root_path:
    :param data_type:
    :param curr_date:
    :return:
    """
    config_filename = get_curr_root_path(root_path,data_type,curr_date) + CONFIG_FILENAME
    if not os.path.exists(config_filename):
        logging.error("ָ������=%s,������������Ϣ!" % (curr_date))
        return False

    with open(config_filename, "r") as f:
       dict =  ast.literal_eval(f.read())

    return dict

def init_config(root_path,data_type,get_type):
    """
    ��ʼ����������ǰ����������Ϣ
    :todo ����ʵ�ֲ���У��
    :param root_path: �ļ��洢��·��
    :param data_type: ���ݲɼ�����  26 ������е  27 ������е
    :param get_type:  ���ݻ�ȡ��ʽ 1 urllib2��ʽ 2 selenium��ʽ
    :return:
    """
    curr_date = file_utils.get_curr_date()
    curr_root_path = get_curr_root_path(root_path, data_type,curr_date)

    #��־��ʼ������
    log_foloder_name =  curr_root_path  + "/logs/"
    file_utils.mkdir_path(log_foloder_name)
    log_utils.log_config(log_foloder_name + LOG_NAME)

    # ��ǰ���ݴ洢��·��(��ʱִ�У� �����ڴ��)
    if os.path.exists(curr_root_path + CONFIG_FILENAME):
        print("�������ݲɼ�[�������л���������Ϣ:%s]:�Ѿ���ʼ���!" % (CONFIG_FILENAME))
        return False

    # ��ʼ���ݴ洢·��
    data_list_folder_name = curr_root_path + "/data_list/"
    data_info_folder_name = curr_root_path + "/data_info/"
    add_folder_name = data_info_folder_name + "/add/"
    reduct_folder_name = data_info_folder_name + "/reduct/"
    data_info_save_folder_name = data_info_folder_name + "/save/"

    # ����list��info�ļ���
    file_utils.mkdir_path(data_list_folder_name)
    file_utils.mkdir_path(data_info_folder_name)

    # ����data_info > add ��reduct �ļ���
    file_utils.mkdir_path(add_folder_name)
    file_utils.mkdir_path(reduct_folder_name)

    # ����save�ļ���(���ջ�������Ϣ)
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

    logging.info("�������л���������Ϣ��ʼ�����:%s" % (config_filename))
    logging.debug(str(config_dict))

def get_last_root_path(root_path,data_type):
    """
    ��ȡ��ǰִ�и�·��: ��ǰ·�� = ���ø�·�� + ��ǰ��������(data_type)  + ��ǰ����
    :param root_path:���ø�·��
    :param data_type:��������
    :return:
    """
    last_date = file_utils.get_last_date()
    last_root_path = root_path + "/" + str(data_type) + "/" + last_date + "/"
    return last_root_path


def get_curr_root_path(root_path,data_type,curr_date):
    """
    ��ȡ��ǰִ�и�·��: ��ǰ·�� = ���ø�·�� + ��ǰ��������(data_type)  + ��ǰ����
    :param root_path:���ø�·��
    :param data_type:��������
    :param curr_date:��ָ������(��ʽ��yyyymm)����ΪNoneʱ�����ɵ�ǰ����
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

