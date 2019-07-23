#coding=utf-8
import ConfigParser

cf = ConfigParser.ConfigParser()

'''
配置文件内容读取
'''
class DataTypeConfig():
    def __init__(self, data_type= str,etc_file = str):
        cf.read(etc_file)
        self.data_type = str(data_type)


    def get_data_type(self):
        return self.data_type

    def get_data_list_url(self):
        return  cf.get(self.data_type,"data_list_url")

    def get_data_info_url(self):
        return  cf.get(self.data_type,"data_info_url")

    def get_total_count(self):
        return  cf.get(self.data_type,"total_count")

    def get_total_page_count(self):
        return  cf.get(self.data_type,"total_page_count")

    def get_save_root_path(self):
        return  cf.get(self.data_type,"save_root_path")

    def get_thread_count(self):
        return  cf.get(self.data_type,"thread_count")






if __name__ == "__main__":
    dataType = DataTypeConfig(26,"../etc/example1_data_type.cfg")

    print("==从配置文件读取内容==: ../etc/example1_data_type.cfg")
    print dataType.get_data_type()
    print dataType.get_data_list_url()
