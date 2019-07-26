# #coding=utf-8
# import os
#
#
#
#
# if  os.listdir('D:/test/'):
#   print('这不是一个空文件夹')
# else:
#   print("这是一个空文件夹:")
#


# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
Function:
【整理】Python中的logging模块的使用（可以实现同时输出信息到cmd终端窗口和log文件（txt）中）
https://www.crifan.com/summary_python_logging_module_usage

Author:     Crifan
Verison:    2012-11-23
-------------------------------------------------------------------------------
"""

import logging;


# -------------------------------------------------------------------------------
def loggingDemo():
    """Just demo basic usage of logging module
    """
    logging.info("You should see this info both in log file and cmd window");
    logging.warning("You should see this warning both in log file and cmd window");
    logging.error("You should see this error both in log file and cmd window");
    logging.debug("You should ONLY see this debug in log file");
    return;


# -------------------------------------------------------------------------------
def initLogging(logFilename):
    """Init for logging
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format = '%(asctime)s - %(levelname)s - %(message)s' ,
        datefmt='%m-%d %H:%M',
        filename=logFilename);
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler();
    console.setLevel(logging.INFO);
    # # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s');
    # # tell the handler to use this format
    console.setFormatter(formatter);
    logging.getLogger('').addHandler(console);


###############################################################################
if __name__ == "__main__":

    logFilename = "E:/data/data_source/26/logs/data_collection.log";
    initLogging(logFilename);
    loggingDemo();