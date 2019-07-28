#coding=gbk
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
# ��ȡ�����ļ�
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")
'''
==============
���ݲɼ�������:�ɼ������б���Ϣ
==============
'''
def save_data_list_to_disk(config_dict):
    data_type = int(config_dict["data_type"])
    get_type = int(config_dict["get_type"])
    data_list_folder_name  =  config_dict["data_list_folder_name"]
    if file_utils.clear_folder(data_list_folder_name):
        logging.info("����ļ����ļ�:%s" % (data_list_folder_name))

    begin_time = time.time()
    logging.info("���ݲɼ���ʼʱ��:%s"  %  (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    # ��ǰ������������
    total_count = comm_utils.get_curr_nmpa_total_count(data_type)
    # ÿҳ��ʾ������(��ÿ���ļ�����1000������)
    page_size = 1000;
    if total_count < page_size:
        page_size = total_count

    # ���㹲����ҳ
    if total_count % page_size == 0:
        total_page_no = total_count / page_size
    else:
        total_page_no = total_count / page_size + 1
    # logging("��������=%s,ÿҳ�ɼ���=%s������%sҳ:" % (total_count,page_size,total_page_no))
    logging.info("��ǰNMPA��������:data_type=%s,��������=%s,ÿҳ�ɼ���%s,����%sҳ" % (data_type, total_count,page_size,total_page_no))
    for index in range(total_page_no):
        page_index = index + 1

        # data_list�����ļ���(�ļ���ҳ��洢��ÿҳPAGE_SIZE��)
        data_list_filename = "data_list_%s_%s.json" % (data_type,page_index)
        data_list_filename = data_list_folder_name + data_list_filename

        # �б�ҳurl(�������ļ���ȡ)
        data_list_url = cf.get("access_url" ,"data_list_url")
        data_list_url = data_list_url.format(data_type, page_index, page_size)
        logging.debug("���ݲɼ���ַ:%s" % (data_list_url))

        # ���ݲɼ������浽����
        data_list_data = access_data_utils.get_data(data_list_url)
        file_utils.write_file(data_list_filename, data_list_data)
        logging.debug("д���ļ��ɹ�:%s" % (data_list_filename))
        logging.info("��%sҳ���ݲɼ����,ʣ��%sҳ,����·��:%s" % (page_index,(total_page_no-page_index),data_list_filename))
        time.sleep(2)
    end_time = time.time()
    logging.info("���ݲɼ�����ʱ��:%s"  % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    logging.info("���ݲɼ����ƺ�ʱ:%s��"  % (end_time - begin_time))



def check_data(config_dict):
    data_list_folder_name = config_dict["data_list_folder_name"]
    data_type = config_dict["data_type"]

    file_list = file_utils.get_file_list(data_list_folder_name)
    id_list = file_utils.get_data_info_id(file_list)
    qsize = id_list.qsize()
    logging.info("���ݲɼ�����=:%s" % (qsize))
    total_count = comm_utils.get_curr_nmpa_total_count(data_type)
    logging.info("��ǰNMPA������������=:%s" % (total_count))

    if qsize == total_count:
        return True
    else:
        return False



def data_collection(config_dict):
    """
    :param config_dict: �������л���������Ϣ
    :return:
    """
    #���ݼ��
    if check_data(config_dict):
       logging.info("data_list���ݼ��Ѿ���ɲɼ�!")
       return


    #���ݲɼ�
    save_data_list_to_disk(config_dict)


#��������ǰ���ɵĻ���������Ϣ
if __name__ == "__main__":
    # if len(sys.argv) <> 3:
    #     print("���г�����Ҫ2������ get_type = {1,2} data_type = {25,26}")
    #     print("����ʾ��:python data_list_collection.py 1 26")
    '''
    ======================================================
    :todo
    get_type: ���ݻ�ȡ��ʽ
            1 urllib2��ʽ
            2 selenium��ʽ
    data_type:���ݲɼ����� 
            26 ������е  
            27 ������е
    root_path:�ļ��洢·��
    =====================================================
    # '''
    #���г����������
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

    #2.��ʼ����־
    log_utils.log_config(curr_root_path + log_name)

    #3.��ʼ�ɼ�
    data_collection(config_dict)

