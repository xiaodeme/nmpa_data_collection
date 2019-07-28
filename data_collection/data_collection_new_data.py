#coding=gbk
import urllib2
import time
import threading
import logging
import sys
import  ConfigParser
reload(sys)
import os
sys.path.append('../')
sys.setdefaultencoding('utf-8')
from utils import access_data_utils
from utils import file_utils
from utils import log_utils
from utils import config
#
# '''
# ==============
# ���ݲɼ�������:��id�ɼ�ע���Ʒ��ϸ��Ϣ
# ==============
# '''
# ��ȡ�����ļ�
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

def start(threadCount,config_dict):
    # ����x���̣߳�����С��10��
    threads = []
    for i in range(threadCount):
        # ���������߳�����
        thread = myThread(i,config_dict)
        # ����̵߳��߳��б�
        threads.append(thread)

    for t in threads:
        t.start()

    # # �ȴ������߳����
    for t in threads:
        if t.isAlive():
            t.join()
    logging.info("�����߳�ȫ������!")


def get_data_info(thread_name,config_dict):
    #�������ݱ���·��
    data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    while not ADD_DATA_LIST.empty():
        try:
            data_id = ADD_DATA_LIST.get()
            info = "�߳���:%s,û�л�ȡ�����ݻ��� %d��" % (thread_name,ADD_DATA_LIST.qsize())
            logging.info(info)

            # data_info�����ļ���
            save_filename = "data_info_thread_%s.json" % (thread_name)
            save_filename = data_info_save_folder_name + save_filename

            # �б�����ҳurl
            data_info_url = cf.get("access_url" ,"data_info_url")
            data_info_url = data_info_url.format(config_dict["data_type"], data_id)

            # ���ݲɼ������浽����
            data_info_data = access_data_utils.get_data(data_info_url)
            data_info_data = data_info_data.replace("\\n\\r", "").decode("gbk").encode("utf-8")

            #�����ݱ�ʶ������һ��洢
            data = str(data_id) + "==" + data_info_data
            with open(save_filename, 'a') as f:
                f.writelines(data + "\n")

            info = save_filename + "д��ɹ�! id: " + str(data_id)
            logging.debug(info)

            # ����1�룬��ֹ�������ж�Ϊ����
            time.sleep(2)
        except urllib2.URLError as e:
            ADD_DATA_LIST.put(data_id)
            print("URLError")
            logging.error("URLError")
            logging.error(e.message)
        except UnboundLocalError as e:
            print("UnboundLocalError")
            logging.error("UnboundLocalError")
            logging.error(e.message)

class myThread(threading.Thread):  # �̳и���threading.Thread
    def __init__(self, name,config_dict=dict):
        threading.Thread.__init__(self)
        self.name = name
        self.config_dict = config_dict
    def run(self):  # ��Ҫִ�еĴ���д��run�������� �߳��ڴ������ֱ������run����
        msg1 = "====Starting " + self.name
        logging.info(msg1)
        get_data_info(self.name,self.config_dict)
        msg2 = "====Exiting " + self.name
        logging.info(msg2)

    def stop(self):
        self.__flag.set()       # ���̴߳���ͣ״̬�ָ�, ����Ѿ���ͣ�Ļ�
        self.__running.clear()  # ����ΪFalse



if __name__ == "__main__":
    # ���г����������
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # �ò�����ʱδ��Ч,δ��������Ҫʵ�ַ�ʽ
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    # 0.��ǰ���ݲɼ��洢·��
    curr_date = file_utils.get_curr_date()
    curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)

    # 1.��ȡ������Ϣ
    config_dict = None
    if not os.path.exists(curr_root_path + config_filename):
        print("�������л���������Ϣ:%s:δ��ʼ������������init.py!" % (config_filename))
        sys.exit(0)
    else:
        config_dict = config.get_config(root_path, data_type, curr_date)

    # 2.��ʼ����־
    log_utils.log_config(curr_root_path + log_name)


    #3. ��ȡ������������
    add_folder_name = config_dict["add_folder_name"]
    add_filename = add_folder_name + "add_data.json"
    ADD_DATA_LIST = file_utils.get_add_data_id(add_filename)
    add_data_count  = ADD_DATA_LIST.qsize()
    logging.info("[data_info]�ɼ�����=%s,�ƻ��������ݲɼ���������=:%s" % (curr_date, add_data_count))

    # data_info > save ���ݲɼ��������
    data_info_save_folder_name = config_dict["data_info_save_folder_name"]
    file_list = file_utils.get_file_list(data_info_save_folder_name)
    data_info_count = file_utils.data_info_count(file_list)
    logging.info("[data_info]�ɼ�����=%s,ʵ���������ݲɼ���������=:%s" % (curr_date, data_info_count))

    if add_data_count == data_info_count:
        logging.info("�ɼ�����=%s,�������ݲɼ��Ѿ����!" %(curr_date))
        sys.exit(0)
    else:
        data_info_save_folder_name = config_dict["data_info_save_folder_name"]
        if file_utils.clear_folder(data_info_save_folder_name):
            logging.info("����ļ����ļ�:%s" % (data_info_save_folder_name))
        start(10,config_dict)