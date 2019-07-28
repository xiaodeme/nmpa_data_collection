#coding=gbk
import logging
import comm_utils
def log_config(log_filename):
    '''
    日志配置：
    可以实现同时输出信息到控制台和log文件中
    :param root_path:
    :param data_type:
    :param log_name:
    :return:
    '''
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_filename);

    #windows调试可用，linux打开不会输出到日志文件
    if comm_utils.is_windows():
        #下方代码可以在本地测试，可同时输出到控制台
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler();
        console.setLevel(logging.DEBUG);
        # # set a format which is simpler for console use
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s');
        # # tell the handler to use this format
        console.setFormatter(formatter);
        logging.getLogger('').addHandler(console);


if __name__ == "__main__":

    LOG_NAME = "data_collection.log"
    log_config("F:/data/" + LOG_NAME)

    logging.debug('这个消息应该到日志文件和控制台')
    logging.info('这应该这样')
    logging.warning('and this，too')

    # stream