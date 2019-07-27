#### NMPA官网数据采集(增量)
- 该包下面程序实现主要目的：数据增量采集
- 每日定时数据采集分析，请运行data_collection_full包的程序

##### 一、使用说明(分步执行)
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
##### 二、执行运行run_all.py程序
```
python run_all.py
```

###  三、定时执行配置
1. 新增定时任务脚本:task.sh
```
#!/bin/bash
python /你的执行脚本全路径/run_all.py
```
2. 执行权限
```
chmod +x task.sh
```
3. 创建定时任务
```
crontab -e
```
新增内容如下：每晚的03:00执行
```
00 03 * * * sh /你的执行脚本全路径/task.sh
```
定时任务相关:https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html
```
crontab -e 新增
crontab -l 查看
crontab -r 删除
```
