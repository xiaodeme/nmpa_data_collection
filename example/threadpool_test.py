#coding: utf-8
import time
import threadpool
import Queue


def init_data():
    list = []
    for x in range(10):
       list.append(x)
    return list



def get_data(q):
    print("===%s" % (q))
    time.sleep(1)
    # while not q.empty():
    #     i = q.get()
    #     msg = "还有%d个数据未获取" % (q.qsize())
    #     print(msg)
    #     time.sleep(1)

if __name__ == "__main__":
    list = init_data()
    # get_data()
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(get_data,list)
    [pool.putRequest(req) for req in requests]
    pool.wait()
#
# def sayhello(str):
#     print "Hello ",str
#     time.sleep(2)
#
# name_list =['xiaozi','aa','bb','cc']
# start_time = time.time()
#
# pool = threadpool.ThreadPool(4)
# requests = threadpool.makeRequests(sayhello, name_list)
# [pool.putRequest(req) for req in requests]
# pool.wait()
# print '%d second'% (time.time()-start_time)