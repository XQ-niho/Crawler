# coding=utf-8

import threading
import time
from day04.threadssecurity import TicketDB

# 创建TicketDB对象
db = TicketDB()

# 线程体1函数
def thread1_body():
    global db
    while True:
        curr_ticket_count = db.get_ticket_count()
        #查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            # 无票退出
            break

# 线程体2函数
def thread2_body():
    global db
    while True:
        curr_ticket_count = db.get_ticket_count()
        # 查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            # 无票退出
            break

def main():
    t1 = threading.Thread(target=thread1_body, name='Thread1')
    t1.start()

    t2 = threading.Thread(target=thread2_body, name='Thread2')
    t2.start()

if __name__ == '__main__':
    main()