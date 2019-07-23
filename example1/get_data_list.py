#coding=utf-8
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from utils import etc_utils
from utils import access_data_utils
from utils import file_utils

#获取配置信息
dataTypeConfig = etc_utils.DataTypeConfig(26,"../etc/example1_data_type.cfg")
save_root_path = dataTypeConfig.get_save_root_path()
total_count = int(dataTypeConfig.get_total_count())

#data_list数据保存路径
DATA_LIST_PATH = save_root_path +  "/data_list/"
file_utils.mkdir_path(DATA_LIST_PATH)

#日志保存路径
LOG_PATH =    save_root_path + "/logs/"
file_utils.mkdir_path(LOG_PATH)

'''
数据采集
'''
def save_data_list_to_disk():
    # 每页显示总数量(即每个文件保存1000条数据)
    page_size = 1000;
    if total_count < page_size:
        page_size = total_count

    # 计算共多少页
    if total_count % page_size == 0:
        total_page_no = total_count / page_size
    else:
        total_page_no = total_count / page_size + 1

    for index in range(total_page_no):
        page_index = index + 1

        # data_list保存文件名
        data_list_filename = "data_list_%s_%s.json" % (dataTypeConfig.get_data_type(),page_index)
        data_list_filename = DATA_LIST_PATH + data_list_filename

        # 列表页url
        app_list_url = dataTypeConfig.get_data_list_url()
        app_list_url = app_list_url.format(dataTypeConfig.get_data_type(), page_index, page_size)


        # 数据采集并保存到本地
        data_list_data = access_data_utils.get_data(app_list_url)
        file_utils.write_file(data_list_filename, data_list_data)

        time.sleep(2)



if __name__ == "__main__":

    #开始采集
    save_data_list_to_disk()

