#coding=utf-8
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
db =  pymysql.connect(
        host='192.168.110.231',
        port=3306,
        user='RA',
        passwd='12345qwert',
        db='RASearchDB',
        charset='utf8'
    )

def get_curr_ids():
    data_id_list = []
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT  a.MEDICAL_DEVICE_INFO_ORIGINAL_ID  FROM   medical_device_base_info a WHERE a.MEDICAL_DEVICE_TYPE = 26"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            data_id_list.append(id)
    except:
        print ("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()

    return data_id_list

if __name__ == "__main__":
    if db <> None:
        print("db connection success!")
    else:
        print("db connection error")

    data_id_list = get_curr_ids()
    print("共计查询数据数量: %s" % (len(data_id_list)))


