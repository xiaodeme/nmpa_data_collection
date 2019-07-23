####  声明：本示例仅做学习研究，若有侵权请通知作者可立即删除。

#### 该示例通过urllib2进行数据采集
```
import urllib2
html = urllib2.urlopen(url).read()
print html
```
#### 数据采集地址：
- data_list_url = http://appcfda.drugwebcn.com/datasearch/QueryList?tableId={0}&pageIndex={1}&pageSize={2}
- data_info_url = http://appcfda.drugwebcn.com/datasearch/QueryRecord?searchF=ID&tableId={0}&searchK={1}

#### 程序说明
example1:
- 配置文件: example1_data_type.cfg
- get_data_list:数据列表数据采集程序
- get_get_info:数据详细信息数据采集程序

#### 使用说明
1. 首先配置example1_data_type相关参数
2. 先运行get_data_list程序
3. 再运行get_get_info程序
4. 按文件最终保存结构查看采集数据
5. 运行check_data查看实际采集数量与配置数据是否相等
6. 保存文件格式均为JSON,可方便入库进一步研究统计
- 文件最终保存结构
```
save_root_path:配置保存的根路径
|---data_list：数据列表信息存放位置
|---data_info：数据详细信息存放位置
|---logs：日志信息
```


#### 其他说明
- 线程数开启太多（实际测试超过50）将被目标服务器拒绝访问，可能是封到了访问IP，建议线程数在10~20左右
- 如果被目标服务器拒绝访问，等待一段时间即可。
