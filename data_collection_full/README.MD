#### NMPA官网数据采集(全量)
- 该包下面程序实现主要目的：当前的数据全量采集，作为每日定时采集对比的基础数据
- 每日定时数据采集分析，请运行data_collection包的程序

1.配置文件： base_config.ini
2.程序运行前配置初始化
```
 python init.py
```   
3.数据列表采集:数据保存路径: /data_list
```
python data_list_collection.py
``` 

4.数据详细信息采集:数据保存路径: /data_info/save/
```
python data_info_collection.py
``` 
5.数据采集检查程序，请查看当前数据采集情况
```
python check_data.py
```
