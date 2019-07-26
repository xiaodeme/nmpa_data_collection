#coding: utf-8
import threading
import time
import Queue

#将cfda数据唯一标识存储到队列里面
q = Queue.Queue()

class Job(threading.Thread):
    def __init__(self, name):
        # super(Job, self).__init__(name)
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print "====Starting " + self.name
        while not q.empty():
            i = q.get()
            msg = "当前线程名:%s,还有%d个数据未获取"%(self.name,q.qsize())
            print(msg)
            time.sleep(2)
        print "====Exiting " + self.name

def initData():
    for x in range(1000):
        q.put(x)
if __name__ == "__main__":

    initData()
    threadList = []
    for i in range(100):
        a = Job("thread="+str(i))
        threadList.append(a)
        a.start()
    for t in threadList:
        t.join()