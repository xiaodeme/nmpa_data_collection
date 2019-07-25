#coding=utf-8
import ConfigParser
from utils import config
from utils import file_utils
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")


# def get_all_data_id(file_list):
#     id_list = []
#     for fileName in file_list:
#         with open(fileName, "r") as f:
#             jsonData = json.loads(f.read())
#             for x in jsonData:
#                 id_list.put(int(x["ID"]))
#     return id_list


def check_save_data():

    # 运行程序基础参数
    get_type = cf.get("base_config", "get_type")  # 该参数暂时未生效
    data_type = cf.get("base_config", "data_type")
    root_path = cf.get("base_config", "root_path")

    config_dict = config.get_config(root_path, data_type)
    data_list_folder_name = config_dict["data_info_save_folder_name"]

    file_list = file_utils.get_file_list(data_list_folder_name)
    print file_list
    id_list = file_utils.get_all_data_id(file_list)




if __name__ == "__main__":
    check_save_data()