# coding=utf-8

#线程安全

import threading
import time

class TicketDB:
    def __init__(self):
        # 机票的数量
        self.ticket_count = 5

    # 获得当前机票数量
    def get_ticket_count(self):
        return self.ticket_count

    # 销售机票
    def sell_ticket(self):
        # TODO 等待用户付款
        # 线程休眠，阻塞当前线程，模拟等待用户付款
        time.sleep(1)
        print('第{0}号票，已经售出'.format(self.ticket_count))
        self.ticket_count -= 1