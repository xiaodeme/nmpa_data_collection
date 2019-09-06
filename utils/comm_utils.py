#coding=utf-8
from utils import etc_utils
from utils import access_data_utils
import json
import  ConfigParser
import platform
# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")
'''
获取NMPA官网当前数据总量
'''
def get_curr_nmpa_total_count(data_type):

    try:
        #访问url
        data_list_url = cf.get("access_url", "data_list_url")
        data_list_url = data_list_url.format(data_type, 1, 1)


        #数据采集
        data_list_data = access_data_utils.get_data(data_list_url)
        jsonData = json.loads(data_list_data)

        return  int(jsonData[0]["COUNT"])
    except BaseException ,e:
        raise e


def is_windows():
    sysstr = platform.system()
    if(sysstr =="Windows"):
        return True

if __name__ == "__main__":



    pass
