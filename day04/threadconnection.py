# coding=utf-8

# 线程间的通信

import threading
import time
import random

# 创建条件变量对象
condition = threading.Condition()

class Stack:
    def __init__(self):
        # 堆栈初始值为0
        self.pointer = 0
        # 堆栈有5个数字的空间
        self.data = [-1, -1, -1, -1, -1]

    # 压栈
    def push(self, c):
        global condition
        condition.acquire()
        # 堆栈已满，不能压栈
        while self.pointer == len(self.data):
            # 等待其他线程把数据出栈
            condition.wait()
        # 通知其他线程把数据出栈
        condition.notify()
        # 数据压栈
        self.data[self.pointer] = c
        # 指针向上移动
        self.pointer += 1
        condition.release()

    # 出栈
    def pop(self):
        global condition
        condition.acquire()
        # 堆栈无数据，不能出栈
        while self.pointer == 0:
            # 等待其他线程把数据压栈
            condition.wait()
        # 通知其他线程压栈
        condition.notify()
        #指针向下移动
        self.pointer -= 1
        data = self.data[self.pointer]
        condition.release()
        # 数据出栈
        return data
