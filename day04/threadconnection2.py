# coding=utf-8

import threading
import time
from day04.threadconnection import Stack

# 创建堆栈对象
stack = Stack()

# 生产者线程体函数
def producer_thread_body():
    global stack

    for i in range(0, 10):
        # 把数据压栈
        stack.push(i)
        print('生产：{0}'.format(i))
        # 没生产一个数字，线程就休眠
        time.sleep(1)

# 消费者线程体函数
def consumer_thread_body():
    global stack

    for i in range(0, 10):
        # 从堆栈中取出数字
        x = stack.pop()
        print('消费：{0}'.format(x))
        time.sleep(1)

def main():
    t1 = threading.Thread(target=producer_thread_body, name='producerThread')
    t1.start()

    t2 = threading.Thread(target=consumer_thread_body, name='consumerThread')
    t2.start()

if __name__ == '__main__':
    main()