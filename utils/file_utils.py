#coding=utf-8
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
fn：写入文件
file_name:文件全路径
data:文件内容
'''
def write_file(file_name,data):
    with open(file_name , 'a') as f:
          f.writelines(data+"\n")
'''
创建文件夹
'''
def mkdir_path(foder_path):
    if  not os.path.exists(foder_path):
        os.makedirs(foder_path)
        print("文件夹创建成功：%s" %(foder_path))
    else:
        print("文件夹：%s 已经存在，不会再创建!" % (foder_path))


'''
获取新增数据标识集合
proccess.py处理后存在
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
    获取文件夹的文件一共有多少行
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
获取所有详细信息标识集合
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
获取文件路径集合
'''
def get_file_list(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L



'''
获取当前数据采集最大页码数
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
    #     print "add_data.json文件不存在，请运行data_process.py程序处理"
    pass