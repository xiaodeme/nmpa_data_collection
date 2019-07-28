#/usr/bin/python
#coding=utf-8
import time

file_name = "/home/txwebadmin/workspace/python/my.log"
data =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open(file_name, 'a') as f:
    f.writelines(data + "\n")