# coding=utf-8
# 继承Thread线程类实现线程体

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name = None):
        super().__init__(name=name)

    #线程体函数
    def run(self):
        # 当前线程对象
        t = threading.current_thread()
        for count in range(5):
            # 当前线程名
            print('第{0}次执行线程：{1}'.format(count, t.name))
            # 线程休眠
            time.sleep(1)
        print('线程{0}执行完成'.format(t.name))

def main():
    # 创建线程一
    t1 = MyThread()
    # 启动线程一
    t1.start()

    # 创建线程二
    t2 = MyThread(name='MyThread')
    # 启动线程二
    t2.start()

if __name__ == '__main__':
    main()