#coding=gbk
import logging
import comm_utils
def log_config(log_filename):
    '''
    ��־���ã�
    ����ʵ��ͬʱ�����Ϣ������̨��log�ļ���
    :param root_path:
    :param data_type:
    :param log_name:
    :return:
    '''
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_filename);

    #windows���Կ��ã�linux�򿪲����������־�ļ�
    if comm_utils.is_windows():
        #�·���������ڱ��ز��ԣ���ͬʱ���������̨
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

    logging.debug('�����ϢӦ�õ���־�ļ��Ϳ���̨')
    logging.info('��Ӧ������')
    logging.warning('and this��too')

    # stream