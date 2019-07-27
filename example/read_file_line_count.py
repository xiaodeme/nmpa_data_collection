#coding=utf-8
import os

"""
读取文件行数
"""
filename = 'E:/data/data_source/26/20190726/data_info/save/data_info_thread_0.json'
count=0
f = open(filename,"r")
for line in f.readlines():
    count=count+1
print count