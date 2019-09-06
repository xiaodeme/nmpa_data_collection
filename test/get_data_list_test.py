# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 0003 15:38
# @Author  : xiaodeme
# @FileName: get_data_list_test.py
# @Software: PyCharm
# @Blog    ：http://www.xiaodeme.cn
from utils import  comm_utils
import ConfigParser


# 读取配置文件
cf = ConfigParser.ConfigParser()
cf.read("../etc/base_config.cfg")

if __name__ == "__main__":

    data_type = cf.get("base_config", "data_type")
    print("当前NMPA官网data_type = %s,数据总量:%s" % (data_type, comm_utils.get_curr_nmpa_total_count(data_type)))
