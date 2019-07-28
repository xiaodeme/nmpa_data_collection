#coding=gbk
from utils import etc_utils
from utils import access_data_utils
import json
import  ConfigParser
import platform
# ��ȡ�����ļ�
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")
'''
��ȡNMPA������ǰ��������
'''
def get_curr_nmpa_total_count(data_type):

    #����url
    data_list_url = cf.get("access_url", "data_list_url")
    data_list_url = data_list_url.format(data_type, 1, 1)
    # print data_list_url

    #���ݲɼ�
    data_list_data = access_data_utils.get_data(data_list_url)
    jsonData = json.loads(data_list_data)

    return  int(jsonData[0]["COUNT"])

def is_windows():
    sysstr = platform.system()
    if(sysstr =="Windows"):
        return True

if __name__ == "__main__":

    data_type = cf.get("base_config","data_type")
    # print("��ǰNMPA����data_type = %s,��������:%s" % (data_type,get_curr_nmpa_total_count(data_type)))
    print is_windows()

    pass
