# coding=utf-8

#线程同步

import threading
import time

from day04.threadssecurity import TicketDB

db = TicketDB()
# 创建Lock对象
lock = threading.Lock()

# 线程体1函数
def thread1_body():
    global db, lock
    while True:
        lock.acquire()
        curr_ticket_count = db.get_ticket_count()
        #查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            lock.release()
            # 无票退出
            break
        lock.release()
        time.sleep(1)

# 线程体2函数
def thread2_body():
    global db, lock
    while True:
        lock.acquire()
        curr_ticket_count = db.get_ticket_count()
        # 查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            lock.release()
            # 无票退出
            break
        lock.release()
        time.sleep(1)

def main():
    t1 = threading.Thread(target=thread1_body, name='Thread1')
    t1.start()

    t2 = threading.Thread(target=thread1_body, name='Thread2')
    t2.start()

if __name__ == '__main__':
    main()