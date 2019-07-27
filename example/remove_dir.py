#coding=utf-8
import shutil
from utils import file_utils
import os
"""
清空文件夹文件
"""




data_list_folder_name = 'E:/data/data_source/26/20190727/data_list'
file_list = file_utils.get_file_list(data_list_folder_name)
for file_name in file_list:
    print os.remove(file_name)