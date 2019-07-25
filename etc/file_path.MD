### file_path.cfg配置文件说明
```
root_path
|
|--data_type
  |
  --20190723  定时每天,按日期存储
    |
    --data_list
    --data_info
    --report    本次采集报告
    --logs
data_info(该文件是通过data_process.py程序处理结果)
|
--add :本次新增的注册产品Id
--reduce：本次减少的注册产品Id
--save：根据add、reduce获取的注册产品完整信息,最终会入库。
```