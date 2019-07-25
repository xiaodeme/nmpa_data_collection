# -*- coding: UTF-8 -*-
import time


# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print time.strftime("%Y%m%d", time.localtime())