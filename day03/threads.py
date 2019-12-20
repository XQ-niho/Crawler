# coding=utf-8

#线程

import threading

#当前线程对象
t = threading.current_thread()
print(t.name)

#返回当前处于活动转态的线程个数
threadCount = threading.active_count()
print(threadCount)

#当前主线程
mainthread = threading.main_thread()
print(mainthread.name)

