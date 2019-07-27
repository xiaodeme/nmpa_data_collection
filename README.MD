## NMPA数据采集程序
用于采集NMPA数据，主要用于研究学习，若有侵权，请联系作者删除:xiaodeme@163.com

## 使用方法
#### 一、运行data_collection_full下程序:该包下程序用于首次生成当前日期的全量数据

1.配置文件： base_config.ini
```
[base_config]
data_type = 26
get_type = 1
root_path = /data/data_source/
```
2.程序运行前配置初始化
```
 python init.py
```   
3.数据列表采集:数据保存路径: /data_list
```
python data_list_collection.py
``` 
4.数据详细信息采集:当前全量数据保存路径: /data_info/save/
```
python data_info_collection.py
``` 
5.数据采集检查程序，请查看当前数据采集情况
```
python check_data.py
```

#### 二、运行data_collection下程序:该包下程序用于按日采集NMPA增量、减量数据
说明：NMPA网站数据每日动态变化，可能新增、亦可能减少数据。所以数据采集逻辑包含新增、减少两个部分

1.配置文件： base_config.ini
```
[base_config]
data_type = 26
get_type = 1
root_path = /data/data_source/
```
2.程序运行前配置初始化
```
 python init.py
```   
3.数据列表采集:数据保存路径: /data_list
```
python data_list_collection.py
``` 
4.数据分析:分析当前日期新增/data_info/add、减少数据/data_info/reduce 
```
python data_process.py
``` 
5.对新增数据进行数据采集
```
python data_collection_new_data.py
```
6.可以检查数据采集情况
```
python check_data.py
```

### 三、数据采集文件夹说明
```
root_path
|
|--data_type
  |
  --20190723  定时每天,按日期存储
    |
    --data_list
    --data_info(该文件是通过data_process.py程序处理结果)
        |
        --add :本次新增的注册产品Id
        --reduce：本次减少的注册产品Id
        --save：根据add分析的数据内容，新采集的注册产品数据。
    --logs: 存放运行日志
    --config.ini 程序运行前生成的配置
```
- 按日期生成，每天一个：定时后续实现，目前手动
- 在/data_info/reduce 用于当前数据新增标识
- 在/data_info/reduce 用于当前数据减少标识
- 在/data_info/save 用于当前数据新增采集注册产信息

### 四、其他说明
- 以上数据可以进一步入库分析