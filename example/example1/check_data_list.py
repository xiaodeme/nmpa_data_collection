#coding=utf-8
from utils import  etc_utils
from utils import  file_utils


#获取配置信息
dataTypeConfig = etc_utils.DataTypeConfig(26,"../etc/example1_get_type.cfg")
save_root_path = dataTypeConfig.get_save_root_path()
total_count = int(dataTypeConfig.get_total_count())

#data_list数据保存路径
DATA_LIST_PATH = save_root_path +  "/data_list/"

if __name__ == "__main__":
     total_count = int(dataTypeConfig.get_total_count())

     file_list= file_utils.get_file_list(DATA_LIST_PATH)
     id_list  = file_utils.get_all_data_id(file_list)

     qsize = id_list.qsize()
     print("采集数据总量:%s" % (qsize))
     print("配置数据总量:%s" % (total_count))

     if qsize == total_count:
          print("Yes!,本次采集数据完整")
     else:
          print("No,本次采集数据可能不完整.请检查并重新采集！")