# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 0009 16:47
# @Author  : xiaodeme
# @FileName: data_list_collection_by_html.py
# @Software: PyCharm
# @Blog    ：http://www.xiaodeme.cn
import os
import sys
sys.path.append('../')
reload(sys)
sys.setdefaultencoding('utf-8')
from utils import config
from utils import access_data_utils
from utils import comm_utils
from utils import log_utils
from utils import file_utils
import logging
import threadpool
import time
import  ConfigParser
from selenium import webdriver
from utils import html_utils
# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

def save_data_list_to_disk2(page_index):


    data_type = int(config_dict["data_type"])
    data_list_folder_name  =  config_dict["data_list_folder_name"]

    # data_list保存文件名(文件按页码存储，每页PAGE_SIZE条)
    data_list_filename = "data_list_%s.html" % (page_index)
    data_list_filename = data_list_folder_name + data_list_filename

    # 列表页url(从配置文件读取)
    data_list_url = cf.get("html_access_url", "data_list_url")
    data_list_url = data_list_url.format(data_type, page_index)
    logging.debug("数据采集地址:%s" % (data_list_url))
    print(data_list_url)




    if comm_utils.is_windows():
        option = webdriver.ChromeOptions()
        option.add_argument('--no-sandbox')
        option.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=option)

        browser.get(data_list_url)
        data_list_data = browser.page_source
        browser.quit()
    else:
        option = webdriver.ChromeOptions()
        option.add_argument('--no-sandbox')
        option.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=option)


        browser.get(data_list_url)
        data_list_data = browser.page_source
        browser.quit()


    file_utils.write_file(data_list_filename, data_list_data)
    logging.debug("写入文件成功:%s" % (data_list_filename))






#程序运行前生成的基础配置信息
if __name__ == "__main__":
    # if len(sys.argv) <> 3:
    #     print("运行程序需要2个参数 get_type = {1,2} data_type = {25,26}")
    #     print("运行示例:python data_list_collection.py 1 26")
    '''
    ======================================================
    :todo
    get_type: 数据获取方式
            1 urllib2方式
            2 selenium方式
    data_type:数据采集类型 
            26 国产器械  
            27 进口器械
    root_path:文件存储路径
    =====================================================
    # '''
    #运行程序基础参数
    config_filename = cf.get("default_config", "config_filename")
    log_name = cf.get("default_config", "log_name")
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效,未来可能需要实现方式
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    #0.当前数据采集存储路径
    curr_date = file_utils.get_curr_date()
    curr_root_path = config.get_curr_root_path(root_path, data_type, curr_date)

    #1.读取配置信息
    config_dict = None
    if not os.path.exists(curr_root_path + config_filename):
        print("程序运行基础配置信息:%s:未初始化，请先运行start.py!" % (config_filename))
        sys.exit(0)
    else:
        config_dict = config.get_config(root_path,data_type,curr_date)

    #2.初始化日志
    log_utils.log_config(curr_root_path + log_name)

    #3.开始采集
    page_size_list = []


    total_page_count, total_count  = html_utils.get_curr_nmpa_total_count(data_type)
    logging.info("当前共计:%s页" % (total_page_count))

    total_page_count = int(total_page_count)
    total_page_count = 5  #测试用
    for index in range(1,total_page_count + 1):
        page_size_list.append(index)
    # print page_size_list

    begin_time = time.time()
    logging.info("数据采集开始时间:%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    thread_max_size = 5   #线程最大数量
    pool = threadpool.ThreadPool(thread_max_size)
    requests = threadpool.makeRequests(save_data_list_to_disk2,page_size_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    end_time = time.time()
    logging.info("数据采集结束时间:%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    logging.info("数据采集共计耗时:%s秒" % (end_time - begin_time))
