#coding=utf-8
from utils import etc_utils
from utils import access_data_utils
import json
'''
获取NMPA官网当前数据总量
'''
def get_curr_nmpa_total_count(data_type):
    dataTypeConfig = etc_utils.DataTypeConfig(data_type, "../etc/example1_get_type.cfg")

    #访问url
    data_list_url = dataTypeConfig.get_data_list_url()
    data_list_url = data_list_url.format(dataTypeConfig.get_data_type(), 1, 1)

    #数据采集
    data_list_data = access_data_utils.get_data(data_list_url)
    jsonData = json.loads(data_list_data)

    return  int(jsonData[0]["COUNT"])


if __name__ == "__main__":

    data_type = cf.get("base_config","data_type")
    # print("当前NMPA官网data_type = %s,数据总量:%s" % (data_type,get_curr_nmpa_total_count(data_type)))


    pass
