#coding=gbk
import os
import  Queue
import json
import datetime
import time


def clear_folder(forder_name):
    file_list = get_file_list(forder_name)
    for file_name in file_list:
        os.remove(file_name)
    return True

'''
fn��д���ļ�
file_name:�ļ�ȫ·��
data:�ļ�����
'''
def write_file(file_name,data):
    with open(file_name , 'a') as f:
          f.writelines(data+"\n")
'''
�����ļ���
'''
def mkdir_path(foder_path):
    if  not os.path.exists(foder_path):
        os.makedirs(foder_path)
        print("�ļ��д����ɹ���%s" %(foder_path))
    else:
        print("�ļ��У�%s �Ѿ����ڣ������ٴ���!" % (foder_path))


'''
��ȡ�������ݱ�ʶ����
proccess.py��������
'''
def get_add_data_id(file_name):
    id_list = Queue.Queue()
    with open(file_name, "r") as f:
        jsonData = json.loads(f.read())
        for x in jsonData:
            id_list.put(x)
    return id_list

def data_info_count(file_list):
    """
    ��ȡ�ļ��е��ļ�һ���ж�����
    :param file_list:
    :return:
    """
    count = 0
    for filename in file_list:
        f = open(filename, "r")
        for line in f.readlines():
            count = count + 1
    return count


'''
��ȡ������ϸ��Ϣ��ʶ����
'''
def get_data_info_id(file_list):
    id_list = Queue.Queue()
    for fileName in file_list:
        with open(fileName, "r") as f:
            jsonData = json.loads(f.read())
            for x in jsonData:
                id_list.put(int(x["ID"]))
    return id_list

'''
��ȡ�ļ�·������
'''
def get_file_list(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L



'''
��ȡ��ǰ���ݲɼ����ҳ����
'''
def get_curr_max_pageno(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(file[0:file.index(".")])

    if len(L) == 0:
        return 0
    else:
        max_pageno = max(L)
        return int(max_pageno)


def get_curr_date():
    return time.strftime("%Y%m%d", time.localtime())

def get_last_date():
    return (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")



if __name__ == "__main__":

    # fname = 'E:/data/data_source/20190724/data_info/add_data/add_data.json'
    # if os.path.exists(format(fname)):
    #     add_data_id = get_add_data_id(fname)
    #     print add_data_id.empty()
    #
    # else:
    #     print "add_data.json�ļ������ڣ�������data_process.py������"
    pass