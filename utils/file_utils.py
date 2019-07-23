#coding=utf-8
import os
import  Queue
import json
'''
fn：写入文件
file_name:文件全路径
data:文件内容
'''
def write_file(file_name,data):
    with open(file_name , 'a') as f:
          f.writelines(data+"\n")
    print(file_name + "文件写入成功!")

'''
创建文件夹
'''
def mkdir_path(foder_path):
    if os.path.exists(foder_path) == False:
        os.makedirs(foder_path)
    else:
        print("文件夹：%s 已经存在，不会再创建!" % (foder_path))
    return True



'''
获取所有详细信息标识集合
'''
def get_all_data_id(file_list):
    id_list = Queue.Queue()
    for fileName in file_list:
        with open(fileName, "r") as f:
            jsonData = json.loads(f.read())
            for x in jsonData:
                id_list.put(x["ID"])
    # msg = "all data_id 都加入队列"
    # print(msg)
    return id_list

'''
获取文件路径集合
'''
def get_file_list(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L


if __name__ == "__main__":
    f = "E:/data_source3/26/test"
    mkdir_path(f)
    pass
